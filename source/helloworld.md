# 第一个`JAVA`程序

话不多说学任何语言都会经历的。`Hello Word!`

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello Word!");
    }
}
```

- 一个`java`文件中有且仅有一个`public class`
  - `public`权限修饰符后面会说到。
  - `class`声明类的关键字。什么是类？什么是关键字？待后面一一道来。
- `main`方法是`java`程序的入口，因此执行逻辑必须有`main`方法
- `static`声明静态的关键字。
- `public static void main(String[] args) `入口方法(函数),若`Java`编程的程序想执行,这个方法必须写
- `{ }` 标记 在标记中书写程序(代码)只要是括号都必须 [成对]出现
-  `;`语句结束的标志。
- `System.out.println("Hello Word!")`打印语句 
- `()`中需要使用 字符串或是变量(常量)或表达式
- `IDEA`开发中可以设置创建`.java`文件自带`main`方法，不过不推荐。我们可以创建完`.java`文件，然后在`public class`公共类中 敲打`main`+`Tab` 会自动给我生成`main`方法

