# Code-MonkeyZhang/ticktick-mcp-enhanced

⭐ 33 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/Code-MonkeyZhang/ticktick-mcp-enhanced) · [官网](https://dida365.com/) · 个人维护 · 中文 README

**让 LLM/Agent 管理滴答清单待办事项的本地 MCP 服务器**

基于滴答清单（TickTick）官方 API 的本地 MCP 服务，Python 3.10+ 实现，面向通过 Claude Desktop 等 LLM 客户端使用 Agent 的用户。公开 20 余个工具，覆盖任务/项目/子任务的创建、更新、移动、批量删除，多维度查询，以及习惯打卡管理；采用运行时 login 工具传入 OAuth 凭据的认证方式，浏览器自动打开授权页，支持中国版/国际版切换，登录状态本地保存。需先在开发者中心注册应用获取 Client ID/Secret。

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

- 20 余个 MCP 工具覆盖任务、项目、查询与习惯管理
- 运行时 OAuth 认证（login 工具），支持中国版/国际版切换
- 任务创建支持智能时间识别，习惯打卡支持批量与补打
- 工具 Prompt 提取为独立 .txt 文件便于维护

## 适用场景

- 在 Claude Desktop 中用自然语言查看和创建待办任务
- 让 AI Agent 批量管理清单、移动任务、查询已完成事项
- 通过对话记录和打卡滴答清单习惯

## 场景标签

 · 领域:效率工具/Agent 集成

## 证据(README 行号)

> L9: 这是一个基于滴答清单官方API的本地MCP服务，能让用户通过LLM和Agent应用轻松管理待办事项
> L87: 此 MCP 向你的 LLM 客户端公开以下工具。

## 星数曲线

```mermaid
xychart-beta
    title "Code-MonkeyZhang/ticktick-mcp-enhanced 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6238a2d0a59d` · [字段定义](../../DATASET.md)*
