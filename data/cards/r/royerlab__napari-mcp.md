# royerlab/napari-mcp

⭐ 46 · Python · BSD-3-Clause · 推送 2026-03-25 · [GitHub](https://github.com/royerlab/napari-mcp) · [官网](https://royerlab.github.io/napari-mcp/) · 组织维护

**通过 MCP 让 LLM 远程控制 napari 图像查看器的服务器**

基于 FastMCP 的 Model Context Protocol 服务器，将 napari 多维图像查看器暴露给 Claude Desktop、Cursor、Cline、Gemini CLI 等 AI 应用，提供 16 个工具覆盖会话管理、图层操作、截图、代码执行与包安装；也可作为 napari 插件运行以控制当前会话。面向显微成像分析场景，pip 安装并用 napari-mcp-install 命令自动配置各 AI 应用。桥接服务器仅绑定 localhost 且无认证，含任意代码执行能力，README 提示仅在受信任本地环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个 MCP 工具覆盖 napari 会话、图层、查看器控制与截图
- 支持 7 种 AI 应用的一键配置（Claude Desktop/Code、Cursor、Cline、Gemini、Codex）
- 可作 napari 插件直接控制当前运行中的查看器会话
- execute_code/install_packages 具任意代码执行能力，服务仅绑定 localhost 且无认证

## 适用场景

- 用对话让 Claude 等 AI 助手加载图像、调整显示并做显微图像分析
- 在 napari 现有会话上接入 AI 助手协助标注与分割
- 用脚本结合 LLM 批量自动化图像处理工作流

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: MCP server for remote control of napari viewers via Model Context Protocol (MCP). Perfect for AI-assisted microscopy
> L99: The server exposes 16 tools for complete napari control:
> L169: - **napari** - Multi-dimensional image viewer

## 星数曲线

```mermaid
xychart-beta
    title "royerlab/napari-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a741c01a9729` · [字段定义](../../DATASET.md)*
