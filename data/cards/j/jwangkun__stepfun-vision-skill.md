# jwangkun/stepfun-vision-skill

⭐ 16 · JavaScript · MIT · 推送 2026-08-03 · [GitHub](https://github.com/jwangkun/stepfun-vision-skill) · 个人维护 · 中文 README

**给 Codex 里的纯文本模型外挂看图能力的 Skill**

Codex Skill 脚本：当主模型（如 DeepSeek deepseek-v4-flash）不支持图片输入时，把粘贴图、本地文件或图片 URL 交给 StepFun step-3.7-flash 多模态模型转成文字描述，主模型再基于描述继续推理与写代码。零依赖 Node.js（Node≥18），一键安装器写入 API key 到 config.json 或环境变量，支持 --latest 从 Codex 会话文件恢复粘贴过的图片、多图与带问题识图；Provider 守卫仅在 deepseek-v4-* 主模型下启用。限制：图片为文字转译、小字与精细布局有损耗，单图上限 25 MB。

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

- 图片经 StepFun step-3.7-flash 转文字描述，供纯文本主模型继续推理
- --latest 从 ~/.codex/sessions/*.jsonl 恢复粘贴过的图片
- 零依赖 Node.js 一键安装器，key 写入 config.json（权限 600）或环境变量
- Provider 守卫仅在 deepseek-v4-* 主模型下启用

## 适用场景

- 用 DeepSeek 等纯文本模型做编程时查看 UI 稿和报错截图
- 把图表/白板照片或票据文档转成文字供主模型处理
- 粘贴图片被主模型忽略后用 --latest 恢复再识别

## 场景标签

`多模态` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8: 给 **纯文本主模型（如 Codex 接入的 DeepSeek `deepseek-v4-flash`）** 外挂“看图”能力的 Codex Skill：
> L22: **怎么解决？** 本 Skill 把图片交给 **StepFun `step-3.7-flash`**（原生多模态推理模型，OpenAI 兼容接口）转成精准的文字描述，再让 DeepSeek 基于描述继续推理、写代码、排障。视觉

## 星数曲线

```mermaid
xychart-beta
    title "jwangkun/stepfun-vision-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `933ad63558e8` · [字段定义](../../DATASET.md)*
