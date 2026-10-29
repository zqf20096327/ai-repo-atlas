# ifmelate/mcp-image-extractor

⭐ 21 · TypeScript · MIT · 推送 2026-02-28 · [GitHub](https://github.com/ifmelate/mcp-image-extractor) · 个人维护

**给 AI 助手用的 MCP 图像提取服务器：转 base64 供 LLM 分析**

一个 MCP server，向 AI 助手（如 Cursor、Claude）提供三个工具：从本地文件、URL 或 base64 数据提取图像并转为 base64，供 LLM 分析；所有图像自动缩放至最大 512x512 以限制输出大小、优化上下文窗口占用。安装方式包括在 .cursor/mcp.json 中用 npx 直接引用、本地路径安装或手动 clone 后 npm 构建，并提供 Docker 构建运行说明。README 列出的适用场景为分析 Playwright 测试截图。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个工具：从本地文件/URL/base64 提取图像并转 base64
- 图像自动缩放至最大 512x512 以优化上下文窗口占用
- 支持 npx 直接在 mcp.json 中引用，无需全局安装
- 提供 Docker 构建与运行说明

## 适用场景

- 让 Cursor/Claude 等 agent 分析本地图片或 URL 图片
- 分析 Playwright 测试的截图结果
- 处理 base64 编码图像供 LLM 使用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: MCP server for extracting and converting images to base64 for LLM analysis.
> L5: This MCP server provides tools for AI assistants to:

## 星数曲线

```mermaid
xychart-beta
    title "ifmelate/mcp-image-extractor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d43a3202637e` · [字段定义](../../DATASET.md)*
