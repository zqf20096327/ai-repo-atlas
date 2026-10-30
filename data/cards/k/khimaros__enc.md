# khimaros/enc

⭐ 16 · Python · GPL-3.0 · 推送 2026-01-29 · [GitHub](https://github.com/khimaros/enc) · 个人维护

**用生成式 AI 把英文代码描述转译为任意编程语言的转译器**

enc 是一个命令行转译器：读取纯英文写的代码描述（*.en 文件），借助生成式 AI 生成对应的其他编程语言源码（示例演示英文转 Rust）。项目自举——其自身由 ./src/enc.en 的英文定义构建，并提供 Python、Rust、C++、TypeScript 等多种版本，默认 Rust 版。支持任意 OpenAI 兼容端点（含 openrouter、llama.cpp），通过 ~/.enc.env 配置 API key。提供 linux-x64 预编译包，也可 git clone 后 make 构建并 make install 按用户级安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 英文描述（*.en）转译为任意编程语言源码
- 自举项目：自身由英文定义 ./src/enc.en 构建
- 提供 bootstrap/Python/Rust/C++/TypeScript 多种实现版本
- 支持任意 OpenAI 兼容端点（含 openrouter 与 llama.cpp）

## 适用场景

- 用英文描述直接生成本地代码文件
- 把英文定义的算法转成 Rust/Python/C++ 等多种语言实现
- 通过自定义 OpenAI 兼容端点（如本地 llama.cpp）离线转译代码

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: `enc` transpiles a plain english description of code to any other
> L8: programming language, with the help of Generative AI.

## 星数曲线

```mermaid
xychart-beta
    title "khimaros/enc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2d82f2f3408c` · [字段定义](../../DATASET.md)*
