1. Use `radare2` to reverse engineer the program:
```
$ radare2 print_flag
[0x080484c0]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x080484c0]> afl
0x080484c0    1 33           entry0
0x08048480    1 6            sym.imp.__libc_start_main
0x08048500    4 43           sym.deregister_tm_clones
0x08048530    4 53           sym.register_tm_clones
0x08048570    3 30           entry.fini0
0x08048590    4 43   -> 40   entry.init0
0x08048880    1 2            sym.__libc_csu_fini
0x080484f0    1 4            sym.__x86.get_pc_thunk.bx
0x08048884    1 20           sym._fini
0x08048820    4 93           sym.__libc_csu_init
0x0804869c    4 92           sym.load_garbage
0x080487ec    1 41           main
0x080485bb   11 225          sym.load_strings
0x08048420    1 6            sym.imp.getenv
0x08048430    1 6            sym.imp.puts
0x08048440    1 6            sym.imp.exit
0x08048470    1 6            sym.imp.strtoul
0x08048460    1 6            sym.imp.srand
0x080484a0    1 6            sym.imp.calloc
0x080486f8   10 201          sym.load_flag
0x08048450    1 6            sym.imp.open
0x08048400    1 6            sym.imp.read
0x080487c1    1 43           sym.print_flag
0x08048410    1 6            sym.imp.printf
0x080483c4    3 35           sym._init
0x080484b0    1 6            sym..plt.got
0x08048490    1 6            sym.imp.rand
[0x080484c0]> s sym.print_flag
[0x080487c1]> VV
```

2. We can see right before the call to printf, the program pushes two strings to the stack:
```
mov dword [var_ch], 0x539; ./print_flag.c:91
mov eax, dword [var_ch]; ./print_flag.c:92
; [0x804a080:4]=0
mov eax, dword [eax*4 + obj.strs]
sub esp, 8
push eax
; const char *format
; 0x804894c
; "your flag is: picoCTF{%s}\n"
push str.your_flag_is:_picoCTF__s
```

3. The part we are interested in is here:
```
mov dword [var_ch], 0x539; ./print_flag.c:91
mov eax, dword [var_ch]; ./print_flag.c:92
; [0x804a080:4]=0
mov eax, dword [eax*4 + obj.strs]
sub esp, 8
push eax
```
4. We can see that it takes `0x804a080` and adds `0x549 * 4` to it. This looks like the memory location of our flag. Lets print it with gbd:
```
$ gdb print_flag core
(gdb) printf "your flag is picoCTF{%s}", *0x804b564
```
