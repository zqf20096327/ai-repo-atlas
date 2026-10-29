# sourcewizard-ai/sourcewizard

⭐ 28 · TypeScript · NOASSERTION · 推送 2026-01-03 · [GitHub](https://github.com/sourcewizard-ai/sourcewizard) · [官网](https://sourcewizard.ai) · 组织维护

**AI 驱动的开发工具/库安装配置向导，支持 MCP**

SourceWizard 是帮助开发者查找、安装和配置软件包与开发工具的智能助手：以自然语言搜索包与代码片段，由遵循自定义安装提示的 LLM 代理执行多包安装与配置，并通过 MCP 集成为 Claude Code 等 MCP 客户端提供 search_packages 与 install_package 两个工具。它检测仓库结构并运行相应构建命令，支持多种包管理器。AI 功能需要 SOURCEWIZARD_API_KEY，以 npm 全局安装的 CLI 与 MCP server 两种形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言的 AI 包搜索
- 遵循自定义 setup 提示的代理式安装器（多包、智能配置）
- 可作 MCP server 提供 search_packages / install_package 工具
- 检测仓库结构并运行对应构建命令

## 适用场景

- 用自然语言查找并安装所需的库和开发工具
- 在 Claude Code 等 MCP 客户端中调用包搜索与安装工具
- 对 Bazel 风格的仓库目标执行构建命令

## 场景标签

 · 领域:开发者工具/包管理

## 证据(README 行号)

> L7: AI-powered setup wizard for dev tools and libraries with MCP (Model Context Protocol) integration.
> L15: SourceWizard is an intelligent assistant that helps developers quickly find, install, and configure packages and de
> L21: - **Agentic AI Installer**: LLM that follows custom setup prompts for multiple packages with intelligent configurat

## 星数曲线

```mermaid
xychart-beta
    title "sourcewizard-ai/sourcewizard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `e54394f508a8` · [字段定义](../../DATASET.md)*
