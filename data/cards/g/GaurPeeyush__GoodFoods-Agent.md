# GaurPeeyush/GoodFoods-Agent

⭐ 23 · Python · 推送 2025-12-22 · [GitHub](https://github.com/GaurPeeyush/GoodFoods-Agent) · [官网](https://www.loom.com/share/ccc0c71369494d50b03bffd3359e5178) · 个人维护

**对话式 AI 餐厅查询订位助手（OpenAI 函数调用）**

面向班加罗尔 GoodFoods 品牌的对话式订位代理：通过 OpenAI GPT-4o 函数调用查找餐厅并经 FastAPI 后端确认订位，前端为 Streamlit 聊天界面，实时展示代理的规划、工具调用参数与结果。提供两个工具（餐厅检索、订位确认），数据以 JSON 文件存储，无外部数据库。限制：无单轮多工具规划、无日期时间校验工具、不支持取消或修改订位、无 OTP 验证。以源码方式运行，`python start.py` 一键启动 API 与 UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI GPT-4o 函数调用驱动餐厅检索与订位确认两个工具
- Streamlit 聊天界面实时展示代理规划与工具调用轨迹
- 护栏机制：最大人数检查、函数文本泄漏检测、占位符检查
- 单命令 `python start.py` 启动 FastAPI 后端与前端

## 适用场景

- 通过对话发现餐厅并完成订位
- 展示 OpenAI 函数调用式代理的构建方式
- 作为品牌客服自动化的原型参考

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L4: GoodFoods is a conversational AI that helps users discover restaurants and book tables across Bangalore. It uses Ope
> L90: - LLM: OpenAI GPT-4o via `openai` SDK

## 星数曲线

```mermaid
xychart-beta
    title "GaurPeeyush/GoodFoods-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `802db779471a` · [字段定义](../../DATASET.md)*
