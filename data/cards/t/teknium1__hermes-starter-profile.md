# teknium1/hermes-starter-profile

⭐ 42 · Python · MIT · 推送 2026-08-09 · [GitHub](https://github.com/teknium1/hermes-starter-profile) · [官网](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions) · 个人维护

**Hermes Agent 的新手入门配置包：关闭系统级工具的精简 profile**

面向零基础用户的 Hermes Agent 配置分发（profile）：通过 hermes profile install 安装后生成独立命令 starter-hermes，提供问答、联网搜索引用来源、图像理解、图像生成与文本转语音能力；刻意屏蔽终端命令、文件改动、浏览器/桌面控制、后台任务与子代理等工具集以降低上手复杂度。模型与提供商由用户自选（推荐 Nous Portal 登录，或 OpenAI/Anthropic/OpenRouter/Google 等），仓库不含 API key。附 profile 审计脚本与 DESIGN.md 工具策略说明；仅缩减工具访问，非操作系统沙箱。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令安装为独立 profile 与快捷命令 starter-hermes
- 保留问答/搜索/图像理解与生成/语音合成，屏蔽终端与文件等系统级工具
- 支持 Nous Portal 免复制 key 登录或自选提供商
- 附带可选的 audit_profile.py 校验工具基线

## 适用场景

- 第一次接触 Hermes Agent，想要不含系统管理工具的精简体验
- 用自然语言做问答、检索引用与写作/规划辅助
- 为演示或试用环境部署能力受限的 agent 配置

## 场景标签

`聊天机器人` `图像生成` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L11: After following the five steps below, you will have a separate command named
> L14: - answer questions and explain unfamiliar topics;
> L17: - generate images;

## 星数曲线

```mermaid
xychart-beta
    title "teknium1/hermes-starter-profile 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-30 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cd1264d41a28` · [字段定义](../../DATASET.md)*
