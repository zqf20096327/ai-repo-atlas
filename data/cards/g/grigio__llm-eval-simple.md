# grigio/llm-eval-simple

⭐ 72 · Python · MIT · 推送 2026-02-28 · [GitHub](https://github.com/grigio/llm-eval-simple) · 个人维护

**通过 OpenAI 兼容接口评测多个 LLM 的轻量基准工具**

Python 编写的 LLM 评测框架：读取 prompts/answers 目录中的文本文件，通过 OpenAI 兼容 API 端点批量测试多个模型，测量响应时间与准确率；正确性判定可选用 AI 评估模型（返回 CORRECT/INCORRECT）或精确字符串匹配。输出逐文件明细表与汇总统计，并附带 REST API 服务器与 Web 仪表盘（前端 npm 运行）可视化结果。依赖 uv 管理环境，要求 Python 3.13+ 与一个可访问的推理端点。

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

- 批量评测多个模型并跟踪响应时间与准确率
- 支持 AI 评估模型或精确字符串匹配两种判定方式
- 生成表格报告并提供 Web 仪表盘可视化
- 通过 .env 配置端点、模型列表与评估模型

## 适用场景

- 在自定义题库上对比多个本地/托管模型的准确率
- 为选型生成带响应时间的基准报告
- 通过 Web 仪表盘查看评测结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: A simple tool for evaluating Large Language Models (LLMs) using a set of prompts and expected answers. It supports t
> L15: - **Flexible Evaluation**: Use AI evaluator models or exact string matching

## 星数曲线

```mermaid
xychart-beta
    title "grigio/llm-eval-simple 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-30 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `5eadbdeb9ae2` · [字段定义](../../DATASET.md)*
