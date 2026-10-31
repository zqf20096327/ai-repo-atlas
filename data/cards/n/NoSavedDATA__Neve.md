# NoSavedDATA/Neve

⭐ 16 · C++ · 推送 2026-10-30 · [GitHub](https://github.com/NoSavedDATA/Neve) · [官网](https://neve-lang.dev/) · 个人维护

**基于 LLVM/C++ 的通用编程语言，Pythonic 语法与并发支持**

Neve 是一门以 LLVM/C++ 实现的高层通用编程语言，采用 Pythonic 语法，提供编译到 C++ 性能级别的产物、高层 JIT、类 goroutine 的线程语法、finish/async 并行表达式，以及 mark-sweep 并发垃圾回收器与 go 风格内存池。安装面向 Linux（Ubuntu 20.04.6+、WSL2 等）：可经 install.sh 脚本装到 ~/.local/neve，或自行安装 clang 19 等依赖后 make 源码构建。示例实现含深度学习（1.4k 行）、BPE、CSV 解析等。附 arXiv 论文与官方文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pythonic 语法，编译产物接近 C++ 性能，另有高层 JIT
- 类 goroutine 线程语法与 finish/async 并行表达式
- mark-sweep 并发垃圾回收器 + go 风格内存池
- 示例含 1.4k 行深度学习实现与 BPE

## 适用场景

- 用接近 Python 的语法编写高性能程序
- 进行并行/并发编程（线程、async 表达式）
- 在语言内实现深度学习等算法原型

## 场景标签

 · 领域:编程语言/编译器

## 证据(README 行号)

> L7: Neve is a LLVM/C++ programming language.
> L59: Deep Learning in 1.4k lines

## 星数曲线

```mermaid
xychart-beta
    title "NoSavedDATA/Neve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `a12dc64fc2ac` · [字段定义](../../DATASET.md)*
