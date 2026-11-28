# charlesknapp/opencode-sidecar

⭐ 5 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/charlesknapp/opencode-sidecar) · [官网](https://www.opencodesidecar.com/) · 个人维护

**VS Code/Cursor 侧边栏 GUI：可视化操作 OpenCode 编码代理**

一个非官方的开源 VS Code 扩展，把本机 OpenCode 2.x 编码代理放入侧边聊天面板：每个提示生成一条时间线，展示思考时长、工具调用输入输出、语法高亮 diff 与子代理实时活动；支持就地应答权限请求与提问、@提及文件/技能/子代理、粘贴图片、fork/rewind 会话、Budget Guard 成本/步数上限。通过 OpenCode v2 HTTP API 连接本地服务，不收集遥测。要求 VS Code 1.95+ 与 OpenCode 2.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每步操作落时间线：思考、工具调用、diff、子代理活动
- 权限请求与提问就地应答，任何操作不代用户自动批准
- 会话 fork、rewind（可含代码回滚）、历史搜索与归档
- Budget Guard 按成本/步数上限停止失控任务

## 适用场景

- 在 VS Code 里以图形界面查看并控制 OpenCode 代理的每一步
- 给子代理设步数/成本上限，防止任务失控
- 在多个编辑器（VS Code/Cursor/VSCodium）间同步同一个 OpenCode 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **An OpenCode chat sidebar and GUI for VS Code.** Sidecar for OpenCode is a free, open-source extension that puts th
> L15: - **Built on OpenCode's own API.** Sidecar talks to the OpenCode 2 service on your machine through its v2 HTTP API.

## 星数曲线

```mermaid
xychart-beta
    title "charlesknapp/opencode-sidecar 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 3 --> 6
    line [4, 5]
```

2026-11-26 4 → 2026-11-28 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `57c21ceea35b` · [字段定义](../../DATASET.md)*
