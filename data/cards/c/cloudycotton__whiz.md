# cloudycotton/whiz

⭐ 277 · TypeScript · MIT · 推送 2026-06-14 · [GitHub](https://github.com/cloudycotton/whiz) · 个人维护

**终端自然语言助手：把英文请求转为可执行命令**

基于 Node.js 的 CLI 工具，用户以 `wz <请求>` 输入自然语言（如抓取网页、打开浏览器、列出 Git 分支），由 OpenAI API 模型生成对应操作。默认模型 gpt-3.5-turbo，可通过 WHIZ_LLM_MODEL 环境变量切换（如 gpt-4），需自行设置 OPENAI_API_KEY。README 明确说明会向 OpenAI 发送 OS 平台、CPU 架构、shell 路径与用户请求本身，不发送文件名或文件内容。面向使用终端的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- wz 命令将自然语言请求转为终端操作
- 默认 gpt-3.5-turbo，支持通过环境变量切换模型
- 隐私说明：仅发送平台/架构/shell 路径与请求，不含文件内容

## 适用场景

- 用自然语言让终端完成抓网页、开浏览器等操作
- 不想记命令语法时用英文描述意图直接执行

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L2:  A copilot for your terminal.
> L24: wz curl google and store response in google.html
> L31: Whiz sends the following information to OpenAI:

## 星数曲线

```mermaid
xychart-beta
    title "cloudycotton/whiz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 276 --> 278
    line [277, 277]
```

2026-10-18 277 → 2026-10-31 277（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c30f9884936e` · [字段定义](../../DATASET.md)*
