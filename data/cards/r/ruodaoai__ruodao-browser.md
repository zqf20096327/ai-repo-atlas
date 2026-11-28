# ruodaoai/ruodao-browser

⭐ 4 · TypeScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/ruodaoai/ruodao-browser) · [官网](https://ruodao.com) · 个人维护 · 中文 README

**给日常浏览者的开源 AI 桌面浏览器：边看边问与网页自动化**

基于 Electron 与 Chromium 的跨平台桌面浏览器，覆盖多标签、书签、历史、下载、无痕窗口、页内查找、独立多开环境等常规浏览器能力。AI 部分包括：侧边栏对话（登录 ruodao.com 或自定义 OpenAI 兼容 base URL）、划词工具条、页面上下文问答、网页操作 Agent（最多 12 步）与 MCP/HTTP 本机接口；发布中心内置 21 个内容平台适配。数据默认仅存本机，无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 侧边栏支持 OpenAI 兼容自定义 base URL 与 API Key
- 内置 MCP（Streamable HTTP/stdio）与 HTTP 直调的 Agent 工具面
- 发布中心适配 21 个内容平台的预检与一键发布
- 独立多开环境，行为对应 Chrome --user-data-dir

## 适用场景

- 浏览网页时随手总结、翻译、解释当前页面
- 让外部 Agent 通过 MCP 操作浏览器完成填表与发布
- 为多账号维护相互隔离的多个浏览器环境
- 向微信公众号、知乎、小红书、X 等平台分发内容

## 场景标签

`AI 助手` `聊天机器人` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: 若道浏览器（Ruodao Browser）是一款**开源、跨平台、基于 Electron 与 Chromium 的 AI 桌面浏览器**，面向「边看边问」的日常浏览场景。
> L14: 它内置若道 AI 侧边栏：登录 ruodao.com 账号（或填入自己的 API Key，支持自定义 base URL / OpenAI 兼容中转站）即可调用云端模型，对当前网页做总结、解释、翻译、改写与多轮问答。同时它把主流浏览
> L60: - 右侧 AI 侧边栏（`Ctrl+Shift+A`），登录或注册 ruodao.com 账号、使用 API Key，直接调用若道云端模型

## 星数曲线

```mermaid
xychart-beta
    title "ruodaoai/ruodao-browser 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `16c2ddf61ba8` · [字段定义](../../DATASET.md)*
