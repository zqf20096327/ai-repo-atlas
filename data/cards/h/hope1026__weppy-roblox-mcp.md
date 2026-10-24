# hope1026/weppy-roblox-mcp

⭐ 68 · PowerShell · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/hope1026/weppy-roblox-mcp) · [官网](https://weppyai.com) · 个人维护

**让 AI agent 直接操作 Roblox Studio 的 MCP 服务器与插件**

由 WEPPY MCP Server 与 Roblox Studio 插件组成：AI 编码代理（Claude Code、Codex、Gemini 等）通过 MCP 连入 Studio，直接创建/修改脚本、实例、地形、光照与资产，变更实时反映在 Studio 与 Dashboard。支持最多五个 Studio 窗口按 Studio ID 路由、通过 Roblox Open Cloud 上传图片资产并应用、本地项目镜像的多向同步、Luau 语法校验与结构化 Playtest。需 Node.js 22+ 与 Roblox Studio；功能分 Basic 与 Pro 层级。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具让 AI 直接在 Studio 内写脚本、改实例、生成地形
- 多 Place 工作流：一个请求路由到最多五个 Studio 窗口
- 本地项目镜像同步与冲突审查
- Luau 语法校验与结构化 Playtest 验证

## 适用场景

- 让 Claude/Codex 等编码代理直接搭建和修改 Roblox 游戏
- 多 Place 项目中一次请求同步更新多个场景
- AI 生成图片资产并上传应用到 Studio

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: > **WEPPY Roblox AI Toolkit** is a Roblox Studio AI development product. It includes the **WEPPY MCP Server** for AI
> L15: The **WEPPY MCP Server** connects AI agents to the **WEPPY Roblox Studio Plugin**. AI directly creates and modifies

## 星数曲线

```mermaid
xychart-beta
    title "hope1026/weppy-roblox-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 65 --> 69
    line [66, 67, 68, 68]
```

2026-10-18 66 → 2026-10-24 68（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ba2dc52e1148` · [字段定义](../../DATASET.md)*
