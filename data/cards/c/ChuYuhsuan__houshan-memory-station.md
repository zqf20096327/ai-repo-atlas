# ChuYuhsuan/houshan-memory-station

⭐ 3 · HTML · MIT · 推送 2026-11-18 · [GitHub](https://github.com/ChuYuhsuan/houshan-memory-station) · 个人维护 · 中文 README

**面向医学考研师生的本地优先 AI 复习与组卷桌面工具**

Electron 单页应用的 Windows 桌面端，分学生端与教师端：学生侧由艾宾浩斯规则引擎排程复习，AI 推荐今日计划、从上传资料生成挖空讲义、错题自动归入知识点单元；教师侧提供 9 类题型组卷工作室、逐题编辑与最多 200 题的后台并发出卷，导出标准 A4 PDF。AI 请求经主进程代理并本地校验 JSON，数据与 API Key 加密存于本机；AI 功能需自行配置模型平台的 API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 艾宾浩斯规则引擎负责复习排程，AI 推荐今日计划与资料挖空
- 教师端 9 类题型组卷、逐题重出、大批量后台出卷（最多 200 题）
- 多平台模型接入：DeepSeek、Kimi、通义千问等及自定义 OpenAI 兼容接口
- 本地优先：数据存 IndexedDB，API Key 经 safeStorage 加密

## 适用场景

- 医学生按遗忘曲线安排长期考研复习
- 从 PDF/Word/PPT 资料生成挖空讲义与练习题
- 教师批量组卷并导出标准 A4 学生卷/教师卷

## 场景标签

`知识库管理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: 面向医学院校教师与长期备考学生的本地优先 AI 复习与组卷工具。
> L5: 规则引擎负责复习节奏，AI 负责今日推荐、资料挖空与题目生成；教师始终保留组卷、改题、重出和导出的最终控制权。
> L42: - 多平台模型：DeepSeek、Kimi、通义千问、智谱 GLM、硅基流动、火山方舟、MiniMax、自定义 OpenAI 兼容接口

## 星数曲线

```mermaid
xychart-beta
    title "ChuYuhsuan/houshan-memory-station 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-02 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `be1bee3288d4` · [字段定义](../../DATASET.md)*
