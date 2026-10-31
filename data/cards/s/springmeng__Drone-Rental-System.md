# springmeng/Drone-Rental-System

⭐ 45 · Vue · Apache-2.0 · 推送 2026-05-26 · [GitHub](https://github.com/springmeng/Drone-Rental-System) · [官网](https://www.javaclimb.com/) · 个人维护 · 中文 README

**AI 无人机租赁全栈实战系统，供毕业设计/课程设计/二次开发学习**

面向租赁业务场景的前后端分离全栈项目：Spring Boot 3 + MyBatis-Plus 后端、Vue 3 + Element Plus 前端，业务覆盖设备浏览、资质审核、下单支付、空域备案、故障报修、维修工单与后台管理。AI 部分：通过 Spring AI 接入 OpenAI Compatible API（含 DeepSeek）实现问答助手，支持 Tool Calling、MCP 对外暴露工具、AI 记忆与会话追踪，可选接入 RAGFlow、Dify/Coze 及 Python LangChain/LangGraph 智能体服务。README 声明禁止商用，需作者授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用户端/管理端双端业务闭环：租赁、支付、空域备案、报修、维修管理
- Spring AI 主链路 + 可选 RAGFlow 知识库降级问答
- MCP / HTTP Tool 对外暴露业务工具能力
- 可选 Python FastAPI + LangChain/LangGraph 智能体服务

## 适用场景

- 毕业设计、课程设计或作品集展示的全栈项目学习
- 学习 Spring AI + MCP + Tool Calling 的工程化集成方式
- 二次开发改造为其他设备/器材租赁系统

## 场景标签

`教程课程` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L15: 本项目是一个适合毕业设计、课程设计、作品集展示和二次开发学习的全栈实战项目，围绕“无人机设备浏览、资质提交、下单租赁、支付管理、空域备案、归还结算、故障报修、后台审核、AI 咨询助手”构建完整业务闭环。
> L33: - 集成 AI 问答助手，可用于设备推荐、规则说明、订单解读
> L117: 本项目采用经典的前后端分离设计，并在业务系统基础上扩展了 AI 能力接入层。

## 星数曲线

```mermaid
xychart-beta
    title "springmeng/Drone-Rental-System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1d92752e12a9` · [字段定义](../../DATASET.md)*
