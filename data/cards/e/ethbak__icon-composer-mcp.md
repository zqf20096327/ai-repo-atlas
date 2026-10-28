# ethbak/icon-composer-mcp

⭐ 62 · TypeScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/ethbak/icon-composer-mcp) · [官网](https://www.npmjs.com/package/icon-composer-mcp) · 个人维护

**为 AI agent 与开发者生成 .icon 图标包的 CLI 和 MCP 服务器**

面向 macOS/iOS 开发者的图标工具：从 PNG/SVG 前景图创建 .icon 包，配置 Liquid Glass 效果（高光、阴影、模糊、半透明）、深色/着色模式变体与背景填充，并导出预览 PNG、App Store 营销图或供 Xcode 使用的包。同时以 MCP 服务器形式提供 12 个工具与 3 个工作流提示词，可接入 Claude Code/Claude Desktop/Cursor/VS Code/Windsurf 等 MCP 客户端。Liquid Glass 渲染依赖 macOS 上的 Apple Icon Composer（ictool）；扁平预览、包编辑与营销导出可跨平台运行。需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 PNG/SVG 创建 .icon 包并配置 Liquid Glass 效果（高光/阴影/模糊/半透明）
- 12 个 MCP 工具 + 3 个工作流提示词，stdio 传输，兼容主流 MCP 客户端
- 深色/着色外观变体的按层级填充与玻璃特效覆盖
- 导出 App Store Connect 营销图（无 alpha，规避 ITMS-90717）与 Xcode 用 .icon 包

## 适用场景

- iOS 26 应用生成带 Liquid Glass 效果的图标包
- 在 Claude Code 或 Cursor 中让 agent 直接创建和调整图标
- 为应用商店上传导出 1024x1024 无透明通道营销图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5:  CLI and MCP server for creating images, icons, and logos with Liquid Glass effects (iOS 26+). Not affiliated with A
> L22: - **AI-agent ready**: 12 MCP tools + 3 workflow prompts with built-in instructions
> L115:  &nbsp;&nbsp; CLI only (no MCP)

## 星数曲线

```mermaid
xychart-beta
    title "ethbak/icon-composer-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-28 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e2a6d6c91efc` · [字段定义](../../DATASET.md)*
