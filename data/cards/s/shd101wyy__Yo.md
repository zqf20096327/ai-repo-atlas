# shd101wyy/Yo

⭐ 39 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/shd101wyy/Yo) · [官网](https://shd101wyy.github.io/Yo/) · 个人维护 · 中文 README

**对 LLM 写入友好、对人类阅读友好的编译型编程语言（进行中）**

Yo 是一门多范式、通用、编译型（转译到 C）编程语言，语法受 Lisp S 表达式启发，定位为 LLM 易写、人类易读，目标性能接近 C。特性涵盖编译期求值、代数效应、async/await、FFI 与 C 互操作、默认内存安全、显式分配器、编译期引用计数与基于 Z3 的形式化验证（契约、精化类型）。项目自述 Work in Progress、Not Ready，标准库仍在设计中。附带 agent skill 文件让 AI 编程代理获取语言知识，CLI 提供中英双语。macOS/Linux/Windows 有安装脚本与预编译编译器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Lisp 风格 S 表达式语法，LLM 与人类双友好
- 契约/精化类型 + 固定版本 Z3 的编译期形式化验证（yo verify）
- 转译到 C，性能目标为比 C 慢 0%-15%
- 内置 agent skill 文件与 AGENTS.md，供 AI 编程代理使用

## 适用场景

- 用一门语法简单、便于 AI 代理生成的语言写程序
- 需要编译期形式化验证与内存安全的系统编程
- 通过 yo init/build/verify 等 CLI 管理项目全流程

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L11: **LLM-friendly to write, human-friendly to read.**
> L238: ## AI Agent Skills

## 星数曲线

```mermaid
xychart-beta
    title "shd101wyy/Yo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8b139fa74b6c` · [字段定义](../../DATASET.md)*
