# ai-shifu/ai-shifu

⭐ 333 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/ai-shifu/ai-shifu) · [官网](https://ai-shifu.com) · 组织维护 · 中文 README

**给创作者/教师提供可自托管的一对一 AI 教学 agent**

AI-Shifu 是面向创作者、教师与企业培训团队的可扩展一对一教学 agent 平台：输入一次专业知识与教学意图，即可生成完整个性化学习路径，按学员背景实时调整讲解、追问、测评与反馈闭环。支持多渠道嵌入网站与课程平台。部署方式以 Docker Compose 自托管为主，提供快速启动、固定版本与开发模式三种 Compose 方案，镜像发布于 Docker Hub 与 GHCR；首个验证用户自动成为管理员，演示用通用验证码默认 1024。LLM 模型通过环境变量编号配置，第 1 个为必填项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 个性化讲解引擎：按学员背景、目标与水平生成学习路径
- 交互式问答与追问：会话中拆解问题、澄清并建议下一步
- 课程快速组装：以高层框架与意图展开为课程、活动与测评
- 多渠道集成：可嵌入网站、课程平台与企业培训门户

## 适用场景

- 把一份课程框架交给 AI-Shifu，让学员获得个性化讲解与实时互动
- 企业录入一次培训内容，员工按角色获得专属学习路径
- 教育者提供大纲生成辅导内容并附带问答助手

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L6: AI-Shifu is designed for creators, instructors, and training/education teams, offering a scalable one-on-one teachin
> L30: AI-Shifu.com is an education platform powered by AI-Shifu. You can try it and learn the AI-guided courses developed
> L123: For the `volcengine` provider, set `VOLCENGINE_TTS_API_KEY` to the API key

## 星数曲线

```mermaid
xychart-beta
    title "ai-shifu/ai-shifu 星数(近 8 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-21", "2026-11-26"]
    y-axis "stars" 325 --> 334
    line [326, 327, 329, 330, 327, 332, 333, 333]
```

2026-10-24 326 → 2026-11-26 333（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `394e0e43bcef` · [字段定义](../../DATASET.md)*
