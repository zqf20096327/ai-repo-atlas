# mirno-ehf/ue5-mcp

⭐ 78 · C++ · MIT · 推送 2026-05-27 · [GitHub](https://github.com/mirno-ehf/ue5-mcp) · 组织维护

**让 AI agent 读写 UE5 蓝图的 MCP 服务器插件**

Unreal Engine 5 编辑器插件，通过编辑器内本地 HTTP 服务器暴露项目蓝图，并配 MCP wrapper 连接 Claude Code 等 AI 工具，使 AI 能读取、修改和创建蓝图、材质与动画蓝图，用户用自然语言描述需求即可操作。编辑器打开时在编辑器进程内运行，关闭时可生成 headless 进程。安装方式为在 Claude Code 中让 AI 按仓库地址自动设置，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UE5 编辑器插件通过本地 HTTP 服务器暴露蓝图
- MCP wrapper 连接 Claude Code 等 MCP 客户端
- 编辑器关闭时可 spawn headless 进程运行
- 支持读取、修改、创建蓝图/材质/动画蓝图

## 适用场景

- 用自然语言让 Claude Code 修改我的 UE5 蓝图
- 批量查找并替换蓝图中的节点调用
- 让 AI 分析现有蓝图系统的逻辑

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Vibe code your Blueprints, materials, and Anim Blueprints. This plugin lets Claude Code (or any MCP client) read, mo
> L19: A UE5 editor plugin exposes your project's Blueprints over a local HTTP server. An MCP wrapper connects that to AI 

## 星数曲线

```mermaid
xychart-beta
    title "mirno-ehf/ue5-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 76 --> 79
    line [77, 78, 78]
```

2026-10-18 77 → 2026-10-28 78（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a67c88e67e8e` · [字段定义](../../DATASET.md)*
