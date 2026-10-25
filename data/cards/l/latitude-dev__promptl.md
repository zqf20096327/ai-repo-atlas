# latitude-dev/promptl

⭐ 104 · TypeScript · MIT · 推送 2026-10-09 · [GitHub](https://github.com/latitude-dev/promptl) · [官网](https://promptl.ai) · 组织维护

**面向 LLM 提示词的动态模板语言，供开发者定义提示**

PromptL 是一种专为 LLM 提示定义设计的模板语言：以人类可读的单一文件定义对话结构（model、temperature 等配置）与消息列表，支持变量插值（如 {{ country_name }}）与动态逻辑。通过通用 WASM 模块加 RPC 提供跨语言支持，官方绑定包括 Python 与 JavaScript，可运行于任何支持 WASM 的语言。以 npm 包 promptl-ai 安装；开发构建使用 pnpm，WASM 模块需先安装 javy 6.0.0 或更高版本。

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

- 单一文件定义 LLM 对话结构与配置，支持变量插值
- 通用 WASM 模块 + RPC，官方提供 Python 等语言绑定
- 以 npm 包 promptl-ai 分发

## 适用场景

- 在应用中按用户输入动态生成 LLM 提示
- 非技术用户以可读格式编写和维护提示模板
- 跨语言项目中复用同一套提示定义

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: PromptL offers a common, easy-to-use syntax for defining dynamic prompts for LLMs. It is a simple, yet powerful lang
> L13: Thanks to our universal WASM module with RPC, you can use PromptL in any language that can run WASM natively or thr

## 星数曲线

```mermaid
xychart-beta
    title "latitude-dev/promptl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-25 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1aa8c2293ed4` · [字段定义](../../DATASET.md)*
