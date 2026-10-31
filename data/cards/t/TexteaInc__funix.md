# TexteaInc/funix

⭐ 125 · TypeScript · MIT · 推送 2026-02-25 · [GitHub](https://github.com/TexteaInc/funix) · [官网](http://funix.io) · 组织维护

**把 Python 函数/类自动转为 Web 应用的开源框架**

Funix 根据函数输入输出的类型自动生成 Web 前端控件，无需手动搭建 UI 即可把普通 Python 函数或类定义变成可通过浏览器分享链接访问的应用。支持 JSON 主题集中定义类型到控件的映射、多页应用与会话管理、yield 流式输出、print/docstring 转入网页、调用历史、prefill 与 token 访问控制；可将 pandas/matplotlib 输出映射为表格与图表，也用于封装 OpenAI 等生成式 AI 调用为 Web 应用。以 pip 包提供，可本地部署，面向 AI/数据方向的开发者与科研人员。

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

- 按变量类型自动生成控件，UI 以 JSON 主题集中配置
- 类定义可转为多页应用，无需手动暴露成员方法
- 支持 yield 流式输出、print/docstring 上屏、会话与调用历史
- 内置 token 访问控制与数据在函数间传递（prefill）

## 适用场景

- 把数据科学或机器学习函数快速做成可分享的 Web 应用
- 给生成式 AI 模型调用套一个网页交互界面
- 科研场景下让别人在浏览器里运行我的模型或算法
- 做多页应用收集人工标注或偏好数据

## 场景标签

 · 领域:AI/数据应用开发工具

## 证据(README 行号)

> L13: * Funix automatically turns an ordinary Python function or class definition into a web app, which is accessible in 
> L21: * Generative AI: instantly allow people to interact your GenAI model or idea.
> L120: You can wrap any Python function into a web app in Funix.

## 星数曲线

```mermaid
xychart-beta
    title "TexteaInc/funix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-31 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d9110ef5f041` · [字段定义](../../DATASET.md)*
