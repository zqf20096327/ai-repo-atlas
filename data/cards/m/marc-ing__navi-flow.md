# marc-ing/navi-flow

⭐ 14 · TypeScript · MIT · 推送 2026-09-02 · [GitHub](https://github.com/marc-ing/navi-flow) · 个人维护 · 中文 README

**Chrome 侧边栏的监督式 AI 浏览器代理，用自然语言执行网页任务**

以 Manifest V3 Chrome 扩展形式运行的 AI 浏览器代理：用户在侧边栏描述任务，系统经规划器分解、执行器操作浏览器（导航/点击/输入/滚动）、验证页面状态后输出结果。设计为监督模式，关键操作前暂停等待批准，记录计划、动作与验证证据供检查；含 Watch Mode 页面监控与工作区隔离。模型接入采用自带 key 的 OpenRouter 通道，密钥存本地不上传。面向需要研究、信息提取、跨页操作且保持人工控制的用户；明确声明非确定性 RPA，不可无人监督用于支付等高风险操作。通过 GitHub 发布未签名 ZIP 手动加载，尚无 Chrome Web Store 渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规划器/执行器/验证器分离的代理运行时结构
- 关键操作前暂停批准，记录可检查的动作与验证证据
- Watch Mode 监控页面变化并报告
- OpenRouter 自带 key 模式，密钥存本地不同步

## 适用场景

- 让 AI 代我读网页、汇总当前页面内容
- 监督下完成跨页面的信息提取与表单准备
- 持续监控某页面并在变化时收到通知

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L23: NaviFlow turns a natural-language request into a supervised browser workflow.
> L56: The supported public configuration is bring your own key through

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/navi-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `b44000106c0a` · [字段定义](../../DATASET.md)*
