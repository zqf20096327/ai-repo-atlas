# mongodb-developer/hr_agentic_chatbot

⭐ 14 · Python · 推送 2026-05-27 · [GitHub](https://github.com/mongodb-developer/hr_agentic_chatbot) · 组织维护

**HR 智能问答聊天机器人：查人事信息并操作 Google 服务**

基于 Chainlit 界面的 HR 聊天机器人项目，由 MongoDB 开发者组织维护。使用 LangChain 编排、OpenAI 语言模型与嵌入 API、MongoDB 存储。附带完整数据管线：脚本生成公司/员工合成数据，调用 OpenAI 生成员工数据嵌入后写入 MongoDB，供聊天机器人检索问答。另通过 OAuth 2.0 接入 Google Drive/Docs/Gmail API，可在对话中操作 Google 服务。需 Python 3.8+、MongoDB、OpenAI API key 与 GCP 账号，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Chainlit Web 界面的 HR 对话问答
- 合成数据生成与 OpenAI 嵌入写入 MongoDB 的数据管线
- OAuth 2.0 接入 Google Drive/Docs/Gmail

## 适用场景

- 企业内部 HR 信息查询问答
- 演示 LangChain+MongoDB 向量检索聊天机器人的参考实现
- 通过对话操作 Google Drive/Docs/Gmail

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This project implements an HR Chatbot using LangChain, MongoDB, OpenAI's language models, and Google APIs. It includ
> L99: To start the HR Chatbot:
> L105:    chainlit run app.py

## 星数曲线

```mermaid
xychart-beta
    title "mongodb-developer/hr_agentic_chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `883449a33670` · [字段定义](../../DATASET.md)*
