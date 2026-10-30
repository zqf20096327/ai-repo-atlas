# djbarrow/fundamental

⭐ 19 · C · GPL-2.0 · 推送 2026-07-06 · [GitHub](https://github.com/djbarrow/fundamental) · 个人维护

**C 语言符号回归工具：暴力搜索常数间关系与数列公式**

命令行 C 程序，通过枚举逆波兰表达式（RPN）的方式暴力搜索公式：用户指定允许的运算符与常量集合，程序从简单表达式逐步向复杂推进，寻找拟合物理常数（如质子/中子质量、黄金比例、精细结构常数）之间关系的等式，也可从 CSV 数据点中找出数列或场的公式。含遗传算法/逐次逼近的尝试性代码、多线程 define 与实验性 CUDA 支持声明。作者自述代码状态不稳定，建议遇问题回退到 2025 年 9 月前版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 基于逆波兰表达式的确定性枚举搜索，保证每个表达式唯一且合法
- 内置物理常量表，可搜索常数之间的关系等式（输出误差值与表达式）
- 支持从 CSV 数据点（多维坐标+场值）归纳公式
- 包含 pthreads 多线程与实验性 CUDA 代码路径

## 适用场景

- 探索物理常数之间是否存在可拟合的数学关系
- 为数值序列或 CSV 采样数据寻找简洁的闭式公式
- 研究整数关系与符号回归的暴力搜索方法

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: Fundamental is a c command line program, a rough diamond which barely works beautifully but is my most original pro
> L151: it is in some ways related to curve fitting ( or more percisely a program for finding integer relations ) where yo
> L159: It uses reverse polish notation (RPN) explained here along with some explanations of the internals of fundamental 

## 星数曲线

```mermaid
xychart-beta
    title "djbarrow/fundamental 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6725bc3f94db` · [字段定义](../../DATASET.md)*
