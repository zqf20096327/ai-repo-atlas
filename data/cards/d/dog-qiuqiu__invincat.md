# dog-qiuqiu/invincat

⭐ 118 · Python · MIT · 推送 2026-05-26 · [GitHub](https://github.com/dog-qiuqiu/invincat) · 个人维护 · 中文 README

**终端原生的 AI 编码助手，带分层记忆与计划执行**

基于 DeepAgents CLI 的 Python 终端 AI 编码助手，面向本地仓库开发者：可读写文件、经审批运行 shell 命令、使用 web/MCP 工具、先出计划再执行（/plan）、维护跨会话的用户/项目两级记忆（由独立记忆 Agent 在回合后提取，可配置专用记忆模型）。内置 explorer/worker/researcher/document-worker 四个子代理，docx/pdf/pptx/xlsx 等技能包，支持自然语言定时任务与企业微信机器人守护进程。需 Python 3.11+，pip 安装，模型经 /model 配置 API key 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用户/项目两级持久记忆，后台记忆 Agent 回合后提取
- 计划先行模式：审批清单后再执行实现步骤
- 四个内置子代理：explorer/worker/researcher/document-worker
- docx/pdf/pptx/xlsx 技能包与 MCP 工具扩展
- 企业微信机器人守护进程接入远程会话

## 适用场景

- 在终端里让 AI 直接修改本地项目代码
- 用计划模式先审查执行步骤再落地多文件改动
- 跨会话保留项目约定与个人偏好记忆
- 通过企业微信远程驱动项目会话与定时任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: Invincat is a terminal-native AI coding assistant for local repositories. It can inspect and edit files, run shell c
> L89: Invincat supports a primary model for normal work and an optional memory model for post-turn memory extraction. If 

## 星数曲线

```mermaid
xychart-beta
    title "dog-qiuqiu/invincat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 116 --> 119
    line [117, 118, 118]
```

2026-10-18 117 → 2026-10-31 118（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `eed1843c0b13` · [字段定义](../../DATASET.md)*
