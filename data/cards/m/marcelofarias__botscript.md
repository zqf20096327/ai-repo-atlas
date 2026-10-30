# marcelofarias/botscript

⭐ 15 · TypeScript · MIT · 推送 2026-09-23 · [GitHub](https://github.com/marcelofarias/botscript) · 个人维护

**面向 LLM 写码场景的 TypeScript 超集语言，编译到 TypeScript**

botscript 是一门编译到 TypeScript 的小型超集语言，设计目标是在'多数代码由机器编写'的语境下，把纯度、副作用能力声明（uses {…}）、穷尽 match、Result/Option 等性质纳入函数签名，从而在编译期阻断 LLM 常见产码错误。提供编译器 CLI、Vite/Babel 插件与 runtime 的 npm 包、浏览器在线 playground、以及供 agent 调用的 MCP server（primer/transform/explain 三个工具）和一次性全栈脚手架提示词。给使用 LLM 生成 TypeScript 代码的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 函数签名级能力声明：空 uses 集合的函数无法访问网络
- match 无 default、as 强制 unsafe 块、Result/Option 取代 try-catch 与 null/undefined
- MCP server 暴露 primer/transform/explain 工具，bot 修复循环无需解析英文错误文本
- 提供 Vite/Babel 插件与 CLI，.bs 文件编译到 .ts

## 适用场景

- 让 LLM agent 生成的 TypeScript 代码在编译期就暴露副作用与错误处理问题
- 在现有 Vite/Babel 项目中渐进引入 .bs 文件
- 通过 MCP server 让 Claude Code 等 agent 直接查询语言规范并迭代修复代码

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: A small TypeScript-superset language for a world where most code is written by
> L120: A botscript-aware bot doesn't need to read this README, the manifesto, or

## 星数曲线

```mermaid
xychart-beta
    title "marcelofarias/botscript 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b8890a3b6bc4` · [字段定义](../../DATASET.md)*
