# breath57/dingtalk-skills

⭐ 102 · Python · 推送 2026-06-26 · [GitHub](https://github.com/breath57/dingtalk-skills) · 个人维护 · 中文 README

**让 AI Agent 用对话操作钉钉的技能库（8 个技能）**

基于 Anthropic skills 规范构建的钉钉 Agent 技能库，覆盖文档/知识库、AI 表格、消息发送、待办、通讯录、网页搜索、日程、知识库搜索等 8 个已上线技能，审批/考勤/会议为计划中。Agent 装载技能后可自动选择钉钉 API 并填参。仅依赖 curl，无需 SDK 或运行时；首次使用时 Agent 引导配置 appKey/appSecret 并写入本地配置文件复用。可经 ClawHub、skills.sh、Hermes 三种方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个已上线技能覆盖钉钉文档、表格、消息、日程、待办、通讯录、搜索
- 仅依赖 curl，无 SDK 或第三方库
- 首次使用自动引导配置并写入 ~/.dingtalk-skills/config 持久复用
- 支持 ClawHub / skills.sh / Hermes 三种安装通道

## 适用场景

- 让 Agent 直接读写钉钉知识库与文档
- 通过对话向群或个人发送钉钉消息
- 用自然语言管理 AI 表格记录、日程与待办

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: 基于 Anthropic skills 规范 构建，**仅依赖 `curl`**，无需安装 Python、SDK 或任何第三方库。安装一行命令，Agent 即可理解"什么时候该调钉钉 API、该调哪个、参数怎么填"，并**自动管理配
> L27: ## 技能纵览
> L31: |dingtalk-document|✅ 已上线|知识库与文档的创建、查询、目录浏览、内容读写、成员管理|🦞 ClawHub · Skills.sh|

## 星数曲线

```mermaid
xychart-beta
    title "breath57/dingtalk-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-27 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3ffaea2dbe2e` · [字段定义](../../DATASET.md)*
