# thesysdev/open-intelligent-ui

⭐ 1,041 · TypeScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/thesysdev/open-intelligent-ui) · [官网](https://www.openui.com/demo/intelligent-ui) · 组织维护

**开源复刻 ChatGPT 智能界面：回答以交互式 UI 流式呈现**

基于 OpenUI（生成式 UI 开放标准）构建的 Next.js 演示应用，复现 ChatGPT Intelligent UI：模型流式输出 OpenUI Lang 程序，由组件原语（布局、文本、输入、图表、地图、SVG 绘图、HTML 沙盒）渲染为交互式答案，含 59 个 @functions 支持答案内计算与状态绑定。默认经 OpenUI Cloud 网关，也可接任意 OpenAI 兼容 API 或通过 Ollama 跑本地模型。需 Node 24；本地模型建议 32 GB 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型流式生成 OpenUI Lang，前端以组件原语渲染交互式答案
- 59 个 @functions 与 $variable 状态绑定，答案内可计算与交互
- 支持 OpenUI Cloud、任意 OpenAI 兼容 API 和 Ollama 本地模型三条路径
- /gallery 提供 16 个示例的手写程序用于开发调试

## 适用场景

- 在自己的应用中构建以交互 UI 呈现的 AI 对话界面
- 本地模型离线运行生成式 UI 演示
- 研究 OpenUI Lang 程序与组件库的组织方式

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: In ChatGPT's Intelligent UI, a request such as "plan a day in San Francisco" returns an interactive answer (a map, p
> L21: The model streams OpenUI Lang 1.0, and the app renders it with a library of primitives the model arranges itself: n

## 星数曲线

```mermaid
xychart-beta
    title "thesysdev/open-intelligent-ui 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 717 --> 1070
    line [746, 770, 791, 807, 822, 846, 853, 867, 874, 884, 893, 898, 807, 959, 970, 977, 986, 991, 996, 1001, 1006, 1014, 1020, 1027, 1036, 1038, 1041, 1041]
```

2026-10-22 746 → 2026-11-24 1,041（+295）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `3c196c80ca7a` · [字段定义](../../DATASET.md)*
