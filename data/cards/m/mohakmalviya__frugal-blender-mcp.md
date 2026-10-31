# mohakmalviya/frugal-blender-mcp

⭐ 15 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/mohakmalviya/frugal-blender-mcp) · [官网](https://pypi.org/project/frugal-blender-mcp/) · 个人维护

**让 AI 代理用 4 个 MCP 工具操控 Blender 建场景**

面向 Claude Code、Codex CLI、Claude Desktop、Cursor、Windsurf 等 MCP 客户端的 Blender 服务器：以 discover/execute/inspect/capture 四个工具覆盖整个 Blender API，固定上下文 338 tokens；通过批量编辑（每次 execute 最多 100 个操作）、惰性 schema 与精简结果压缩 token 消耗。以 Blender 插件加 Python 桥接形式运行，权限分级（delete/save/python 默认关闭），桥接仅监听回环并需随机 token，另提供无 uvx 的源码安装与 CLI 脚本驱动方式。

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

- 4 个 MCP 工具覆盖全 Blender API，固定上下文 338 tokens
- 单次 execute 批量携带最多 100 个操作
- 权限门控：delete/save/python 默认关闭，回环监听加随机 token
- 提供 CLI 以相同代码路径脚本化驱动 Blender

## 适用场景

- 让 Claude Code 或 Cursor 中的代理代为搭建与渲染 Blender 场景
- 在代理工作流中用脚本批量执行 Blender 操作并捕获预览
- 需要限制代理危险操作权限的自动化 3D 制作

## 场景标签

 · 领域:3D 制作/开发者工具

## 证据(README 行号)

> L33: Frugal Blender MCP exposes four tools, **`discover`**, **`execute`**, **`inspect`** and **`capture`**,
> L54: claude mcp add blender -- uvx frugal-blender-mcp
> L194: AI client -- MCP stdio --> Python bridge -- authenticated loopback JSON --> Blender add-on

## 星数曲线

```mermaid
xychart-beta
    title "mohakmalviya/frugal-blender-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28", "2026-10-31"]
    y-axis "stars" 12 --> 16
    line [13, 14, 15, 15]
```

2026-10-18 13 → 2026-10-31 15（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f2653682e5dc` · [字段定义](../../DATASET.md)*
