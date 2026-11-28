# tumourlove/monolith

⭐ 380 · C++ · MIT · 推送 2026-11-19 · [GitHub](https://github.com/tumourlove/monolith) · [官网](https://github.com/tumourlove/monolith/wiki) · 个人维护

**UE5 编辑器 MCP 插件：让 AI 助手读写蓝图/材质/动画等项目资源**

Unreal Engine 5.7/5.8 的编辑器 MCP 插件，让支持 MCP 的 AI 助手（Claude Code、Cursor、Cline 等）读取和编辑项目中的蓝图、材质、动画、Niagara、UI、音频、网格体及引擎源码查询等。设计上不注册数百个独立工具，而是把约 1,500 个动作收纳在 27 个命名空间之后，AI 通过 `monolith_discover()` 按需发现，节省上下文。通过 Releases zip 或源码安装，配置 `.mcp.json` 后由编辑器启动 MCP 服务器（端口 9316）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 1,500 个动作覆盖蓝图、材质、动画、Niagara、GAS、音频等 27 个命名空间
- 以 `{namespace}_query` 查询工具替代大量独立工具注册，减少 AI 上下文占用
- 提供 Reflection Intelligence（决策/风险/C++ 反射/复制查询）
- 提供 Releases 预编译 zip 与源码构建两种安装方式

## 适用场景

- 让 Claude Code / Cursor 直接读取并修改 UE 项目资源
- 通过 MCP 为 AI 助手接入 Unreal 编辑器的工具集
- 按命名空间查询引擎反射与项目结构信息

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Monolith is an Unreal Engine editor plugin that lets your AI assistant (Claude Code, Cursor, Cline, or anything else
> L9: I started it because every Unreal MCP setup I tried registered hundreds of separate tools, and the AI burned half it

## 星数曲线

```mermaid
xychart-beta
    title "tumourlove/monolith 星数(近 18 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-14", "2026-11-18", "2026-11-19", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 346 --> 383
    line [350, 352, 353, 355, 358, 361, 360, 361, 349, 367, 370, 371, 372, 374, 375, 379, 380, 380]
```

2026-10-26 350 → 2026-11-28 380（+30）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `6e803517a7f8` · [字段定义](../../DATASET.md)*
