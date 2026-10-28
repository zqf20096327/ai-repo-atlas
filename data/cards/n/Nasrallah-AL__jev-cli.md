# Nasrallah-AL/jev-cli

⭐ 22 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Nasrallah-AL/jev-cli) · [官网](https://jevcli.vectorz.app/) · 个人维护

**调用 TypeSafe Jev 模型做 AI 判断的命令行工具**

npm 安装的命令行客户端（命令名 jev），封装 TypeSafe 托管的 Jev 模型：用户给出内容与固定答案集，模型返回各答案的概率，提供 verify 事实核验、screen 提示注入检测、classify、extract、find、rerank、route、compact 等 13 个子命令，支持管道、JSON 输出与 CI 门禁（退出码 2）。密钥存于系统钥匙串，也可 npx 免安装运行。另附带 Claude Code 插件。需 Node.js 20.12+ 与 TypeSafe API key。

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

- 13 个子命令覆盖核验/分类/抽取/重排/路由等判断任务
- 退出码约定使其可作为 CI 门禁与 agent 守卫
- API key 存储于 OS 钥匙串，支持 npx 免安装运行
- 附带 Claude Code 插件，提供 /jev:* 命令与 compaction 钩子

## 适用场景

- 在 CI 中对文案声明做事实核验门禁
- 检测输入文本是否试图劫持 AI agent
- 对检索结果重排或在多条记录间去重匹配

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: Fast, typed AI judgments from the command line, powered by TypeSafe's Jev model.
> L10: Jev does not write text. You give it content and a question with a fixed set of answers, and it returns a probabili
> L12: Installed from npm as **`jevctl`**. The command is **`jev`**. Website: jevcli.vectorz.app.

## 星数曲线

```mermaid
xychart-beta
    title "Nasrallah-AL/jev-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `90da9cd80063` · [字段定义](../../DATASET.md)*
