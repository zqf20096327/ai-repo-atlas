# guoxinxin20252025/workflowagent

⭐ 50 · TypeScript · NOASSERTION · 推送 2025-12-22 · [GitHub](https://github.com/guoxinxin20252025/workflowagent) · 组织维护 · 中文 README

**自然语言生成 Dify 工作流的 Agent 功能（基于 Dify 二开）**

基于 Dify 1.10.0 二次开发的项目，在工作流编辑器中嵌入对话式 Agent：用户用自然语言描述需求，Agent 通过 LLM 推理与工具调用自动选择节点、填写 System Prompt 与参数、完成连线和变量引用，生成可直接运行的 Dify 兼容工作流；运行报错可反馈给 Agent 重新编排。面向不熟悉节点逻辑的运营等非技术人员与 Dify 用户。通过预构建 Docker 镜像和一键脚本部署，需自行配置 Agent 模型的 Base URL/API Key/Model Name，README 提示需人工审查生成结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话即搭建：自然语言自动选节点、填参数、连线与变量引用
- 生成结构直接兼容 Dify 标准，导入即可运行并支持继续微调
- 运行错误反馈给 Agent 可重新编排渲染到画布
- Docker 预构建镜像 + Windows/Linux/macOS 一键启动脚本

## 适用场景

- 不会节点逻辑的运营/销售人员用一句话搭建 Dify 工作流
- 通过多轮对话迭代修改已生成的工作流
- 把运行错误发给助手让其自动修复编排

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: >本项目基于 Dify 进行二次开发，遵循 Apache License 2.0 协议。非常感谢 Dify 团队提供的优秀开源底座，让构建工作流变得如此简单。
> L178: Workflowagent 采用经典的 Agent + Tools 架构，通过 LLM 的推理能力和工具调用机制，实现自然语言到工作流的自动转换。

## 星数曲线

```mermaid
xychart-beta
    title "guoxinxin20252025/workflowagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ae241867922f` · [字段定义](../../DATASET.md)*
