# alvinxx1123/sspOffer-interview-assistant

⭐ 99 · Java · MIT · 推送 2026-08-26 · [GitHub](https://github.com/alvinxx1123/sspOffer-interview-assistant) · 个人维护 · 中文 README

**互联网面试准备一站式平台：AI 面试模拟与面经整合**

基于 LangChain4j + Spring Boot + React + Electron 的面试准备应用，面向互联网求职者。功能覆盖面经搜索与图片解析录入、简历与投递管理、基于面经库 RAG 的 AI 面试模拟（深挖题生成、连续追问、SSE 流式输出、整场评分与历史对比）、面经复盘、在线算法 IDE（Piston 执行 Java/Python/Go）、实习项目概念掌握度诊断，并通过 Function Calling 让模型调用查面经/查题/运行代码等后端能力。提供桌面端安装包、Web 端（mvn spring-boot:run）与 npm CLI 三种形态；LLM 默认走 DeepSeek，可切换任意 OpenAI 兼容服务，未配置 Embedding 时 RAG 降级为关键词搜索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面经库 RAG + 简历生成 9–12 道深挖题，SSE 流式输出
- 连续面试追问、整场评分与历史表现对比
- Function Calling 调用查面经/查算法题/运行代码/统计高频考点
- Skill Pack 架构将规则与模板抽离为 Markdown，调优无需重新编译

## 适用场景

- 生成针对目标公司/岗位的模拟面试题并进行连续追问训练
- 上传真实面经获得结构化复盘与改进建议
- 上传项目文档生成 STAR 经历与概念掌握度诊断
- 本地管理面经、简历、投递进度并在线刷算法题

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L6: 基于 LangChain4j + Spring Boot + React + Electron 的面经整合与 AI 面试准备应用。支持面经搜索、AI 面试模拟（RAG + 深挖题 + 连续追问 + 整场评分 + 历史对比）、面试复盘
> L90: - **深挖题生成**：根据目标公司 / 部门 **面经库 RAG** + 简历生成 **9–12 道深挖题**，覆盖实习 / 项目 / Java 八股 / AI/Agent/LLM / 算法等方向

## 星数曲线

```mermaid
xychart-beta
    title "alvinxx1123/sspOffer-interview-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 98 --> 100
    line [99, 99]
```

2026-10-18 99 → 2026-10-23 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0fdc21fba613` · [字段定义](../../DATASET.md)*
