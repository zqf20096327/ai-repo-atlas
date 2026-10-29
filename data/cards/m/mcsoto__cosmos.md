# mcsoto/cosmos

⭐ 177 · Prolog · 推送 2026-10-14 · [GitHub](https://github.com/mcsoto/cosmos) · [官网](https://cosmos-lang.github.io/) · 个人维护

**运行于 SWI-Prolog 的自宿主函数-逻辑编程语言**

Cosmos 是一门关系型/函数-逻辑多范式编程语言，由 compiler/src 中的自宿主编译器编译，运行于 SWI-Prolog 之上，无 Lua 依赖。v1 提供函数-逻辑核心，支持表和类 JSON 结构；v2 计划支持命令式风格与静态类型/模式检查，测试组通过含 WASM。通过 make exe 构建可执行文件，支持 REPL、类、协议、模块与 xpce 图形库。整体程序推理与导入接口尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自宿主编译器，运行于 SWI-Prolog，无 Lua 依赖
- 函数-逻辑核心，支持表与类 JSON 结构
- 静态类型/模式检查与协议确定性检查
- 编译目标含 WASM（14 个测试组通过）

## 适用场景

- 用逻辑/关系编程范式编写程序
- 通过 REPL 交互式查询变量解
- 在 SWI-Prolog 平台上构建与扩展语言应用

## 场景标签

 · 领域:编程语言/编译器

## 证据(README 行号)

> L14: A relational programming language.
> L65: Cosmos is compiled by the self-hosted compiler in `compiler/src`

## 星数曲线

```mermaid
xychart-beta
    title "mcsoto/cosmos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 176 --> 178
    line [177, 177]
```

2026-10-18 177 → 2026-10-29 177（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `cdd40389b9f1` · [字段定义](../../DATASET.md)*
