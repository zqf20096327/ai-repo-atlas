# contour-terminal/endo

⭐ 31 · C++ · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/contour-terminal/endo) · [官网](https://contour-terminal.github.io/endo/) · 组织维护

**跨平台 F# 风格函数式编程 shell 与脚本语言**

Endo 是运行于 Linux/macOS/Windows 的交互式 shell 与脚本语言，将 F# 的函数式编程（管道、模式匹配、代数数据类型、类型推断）与 Bash 兼容的命令行约定结合。结构化管道在阶段间传递类型化记录，git log 等命令返回结构化数据，补全由类型系统驱动。实验性 AI agent 功能默认关闭，源码构建需 -DENDO_ENABLE_AGENT=ON 开启。项目处于早期开发阶段，语言与 API 可能变动。安装提供 .deb 包与源码 CMake 构建，Homebrew/Scoop/RPM 在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 结构化管道传递类型化记录，命令返回结构化数据
- F# 风格：模式匹配、Option/Result、类型推断、不可变绑定
- Bash 兼容：重定向、glob、&&/||
- 实验性 AI agent 功能，源码构建默认关闭

## 适用场景

- 用函数式风格做命令行数据管道处理
- 编写跨 Linux/macOS/Windows 的可移植 shell 脚本
- 在 shell 中获得类型检查与类型感知补全

## 场景标签

 · 领域:终端/开发工具

## 证据(README 行号)

> L14: > **Early Development** — Endo is under active development. The language, builtins, and APIs
> L143: The experimental AI agent features are off by default in a source build; add
> L144: `-DENDO_ENABLE_AGENT=ON` at configure time to include them. The packages below are built

## 星数曲线

```mermaid
xychart-beta
    title "contour-terminal/endo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bee7d44fb87b` · [字段定义](../../DATASET.md)*
