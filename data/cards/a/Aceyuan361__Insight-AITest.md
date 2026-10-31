# Aceyuan361/Insight-AITest

⭐ 21 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/Aceyuan361/Insight-AITest) · [官网](https://github.com/Aceyuan361/Insight-AITest) · 个人维护 · 中文 README

**模块化 AI 测试与监控平台：性能监控、AI 测试用例生成、API/UI 自动化**

面向测试开发者的插件式平台：平台内核扫描 manifest.yaml 装配模块，React 前端按清单渲染。六大模块覆盖 Android/iOS 真机性能监控（WebSocket 实时 CPU/内存/FPS）、本地 RAG 知识库问答、AI 测试用例生成（分析→选点→生成→评审）、多步 API 自动化与基于 Midscene 视觉模型的浏览器 UI 自动化。无 LLM key 时性能监控可独立运行；AI 模块通过环境变量配置 OpenAI 兼容 API。Windows 提供 start.bat 一键启动。

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

- Android/iOS 真机实时性能监控（CPU/内存/FPS/网络/电池）
- AI 测试用例生成：分析场景→选测试点→结构化生成→人工评审
- Midscene 视觉 LLM 驱动的浏览器自动化（aiAction/aiAssert/aiQuery）
- 本地 RAG 知识库：文档上传+本地向量索引

## 适用场景

- 连接手机实时监控 App 的 CPU/内存/FPS 并设告警阈值
- 上传项目文档后用 AI 助手基于自有知识库问答
- 自然语言描述测试场景，让 AI 生成并执行 API/UI 测试用例

## 场景标签

`浏览器自动化` `文档问答` · 领域:效率与自动化

## 证据(README 行号)

> L34: > **v2.0.0 ships six core modules (A–F) plus a knowledge-base module, all complete:**
> L51: - **Test-case generation**: AI analyzes scenarios and proposes structured test cases for review.
> L143: export INSIGHT_EYE_AI_LLM_BASE_URL=https://api.example.com/v1

## 星数曲线

```mermaid
xychart-beta
    title "Aceyuan361/Insight-AITest 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7e87ca62972f` · [字段定义](../../DATASET.md)*
