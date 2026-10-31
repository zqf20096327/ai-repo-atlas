# hypercycle-development/mosaic-companion

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/hypercycle-development/mosaic-companion) · 组织维护

**桌面端 AI agent 运行时：多模型对话+沙箱工具与插件工作区**

HyperCycle 开发的开源 Electron 桌面应用，以浏览器式标签页界面与多家 AI 提供商（Claude、OpenAI、Gemini、Ollama、HyperCycle 及自定义端点）的 agent 对话，同时作为扩展这些 agent 能力的运行时：通过 MCP 连接服务器、经 Extism 沙箱化并声明权限的 WebAssembly 工具、受权限约束的渲染器插件、本地 Vault 存储、Web3 钱包功能及内置代码编辑器。项目自述为 pre-1.0，接口与安全边界仍在变动，Vault 内容以明文 JSON 存储未加密。提供三平台安装包与源码运行两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多家提供商（Claude/OpenAI/Gemini/Ollama/自定义端点）的 agent 对话与工具调用
- 沙箱 WASM 工具（Extism）+ MCP 连接 + 受权限约束的渲染器插件三种扩展形态
- 插件目录发布带签名校验，人工审查源码
- 内置代码编辑器、终端与 MosaicBot 后台助手

## 适用场景

- 在一个桌面工作区里同时使用多家 AI 提供商的 agent
- 通过 MCP 与沙箱工具扩展 agent 的能力
- 以权限模型运行第三方插件并查看每工具活动日志

## 场景标签

`AI 助手` `聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: It is also a runtime for extending what those agents can do: sandboxed WebAssembly tools, Model Context Protocol con
> L33: - Multiple AI agents using Claude, OpenAI, Gemini, Ollama, HyperCycle, or custom endpoints.

## 星数曲线

```mermaid
xychart-beta
    title "hypercycle-development/mosaic-companion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4942b99b7843` · [字段定义](../../DATASET.md)*
