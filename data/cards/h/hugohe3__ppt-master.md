# hugohe3/ppt-master

⭐ 63,435 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/hugohe3/ppt-master) · [官网](https://hugohe3.github.io/ppt-master-examples/) · 个人维护 · 中文 README

**给 AI agent 用户的工具：从文档或主题生成本地可编辑的原生 PPT**

一个以 skill/工作流形式交付的开源项目：用户在具备 agent 能力的 AI 工具（IDE 插件、CLI 等）中给出文档或主题，工作流在本地运行并导出可编辑的 .pptx，包含原生形状与连接符、带数据的图表与表格、切换与动画、基于演讲者备注的旁白音频，并支持自有 .pptx 模板。需自行安装 Python 3.10+ 并依赖依赖文件安装包；文档另说明旧格式需可选 Pandoc。模型质量由所用 LLM 决定，推荐大上下文窗口模型并搭配 AI 图像生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.8 天,年发版 36,25 位贡献者
- 涨星:近 1 天 **+511**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800

## 能力要点

- 生成本地可编辑 .pptx：原生形状、母版/版式继承、带数据图表与表格
- 支持从参考中提炼品牌/风格/版式模板，填充既有 .pptx 并保留设计
- 为成品幻灯片添加原生切换、动画与旁白音频
- 流程在本地机器运行，除模型通信外数据不离开本机

## 适用场景

- 把 PDF/DOCX 等资料转成可继续编辑的 PPT 初稿
- 用公司自有模板批量生成汇报文稿
- 为讲稿自动生成旁白与动画效果

## 场景标签

 · 领域:办公/文档自动化

## 证据(README 行号)

> L69: In form, it's a workflow (a "skill") that runs inside any agent-capable AI tool: tell it in chat — "make a deck fro
> L77: - **No platform lock-in** — any agent-capable AI IDE can drive it; Claude, GPT, Gemini, Kimi, and other models all 
> L83: > `harness + model = agent` — PPT Master only owns the workflow; the model sets the ceiling. Recommended: **Kimi K3

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `cdd5be3c7c33` · [字段定义](../../DATASET.md)*
