# jiawei686/wechat-dev-mcp

⭐ 18 · JavaScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/jiawei686/wechat-dev-mcp) · 个人维护 · 中文 README

**让 AI 客户端自动调试微信小程序/小游戏的 MCP 服务器**

基于微信开发者工具自动化端口的 MCP 服务器：向 Claude Code、Cursor、Cline、Zed 等 MCP 客户端暴露截图、模拟触控、canvas 导出、读 console/网络日志、一键重开重编译等工具，用户以自然语言指示 AI 完成调试流程。需本机装微信开发者工具并开启服务端口、Node.js ≥ 18，通过 npx 运行。已知限制：页面截图不含 canvas 内容（需用 export_canvas）、有状态调用一条消息只发一个、日志仅从连接时刻起收集。配套 wechat-dev-skill 可自动巡检四来源报错。

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

- 截图与 export_canvas 画布真实内容导出
- 模拟点击/长按/滑动，小游戏落子自动坐标补偿
- 读取 console/vConsole/网络请求日志定位报错
- 一键重开并重新编译，避开易崩的 Page.reload

## 适用场景

- 对 AI 说人话即可让其在微信小程序上跑流程并截图核对 UI
- 调试小游戏时让 AI 落子、导出画布、抓日志
- 配合 wechat-dev-skill 一句话自动扫描四来源报错

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L17: 兼容 WorkBuddy、Claude Code、Cursor、Cline、Zed 等任意 MCP 客户端。
> L56: - 📸 **截图**：小程序页面 / 小游戏画布实时截图

## 星数曲线

```mermaid
xychart-beta
    title "jiawei686/wechat-dev-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `192914c060c5` · [字段定义](../../DATASET.md)*
