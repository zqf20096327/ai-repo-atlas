# AyanTouqeer/ValencePack

⭐ 5 · JavaScript · 推送 2026-11-10 · [GitHub](https://github.com/AyanTouqeer/ValencePack) · [官网](https://valencepack-682316977612.asia-south1.run.app) · 组织维护

**面向欧盟市场的可持续包装合规决策支持工具**

以证据为基础的包装决策支持应用：用户输入产品、现有包装、目的地、预算与优先级后，系统先用确定性规则引擎筛除不合规选项（无 AI 参与），再按用户优先级加权打分排序，最后调用 Google Cloud Vertex AI 上的 Gemini，仅基于提供的证据包生成解释、标注声明类型、剥离虚构引用 ID；Gemini 失败时回退到规则文本。可部署至 Cloud Run 并用 Firestore 存储报告。由 AI Builder Cup 2026 参赛团队开发，提供本地运行与云端部署说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性规则引擎筛选，规则 ID 透明可查，筛选阶段不涉及 AI
- Gemini 解释被限制在证据包内，仅允许引用提供的来源 ID
- Gemini 失败时回退到规则文本
- 可选 Firestore 存储报告，支持 Cloud Run + Firebase Hosting 部署

## 适用场景

- 评估包装方案是否符合欧盟可持续合规要求
- 按预算与优先级获得可解释的包装改进排序
- 需要 AI 解释可追溯到证据来源的合规筛查场景

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L21: 1. **Screening** — `lib/screen.js` removes unsuitable options using explicit rule IDs: `R-REFORMULATION`, `R-END-OF
> L23: 3. **Explanation** — `lib/rag.js` and `lib/gemini.js` use Google Cloud Vertex AI (lazily initialized). Gemini is in

## 星数曲线

```mermaid
xychart-beta
    title "AyanTouqeer/ValencePack 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-11-01", "2026-11-27"]
    y-axis "stars" 2 --> 6
    line [3, 5, 5]
```

2026-10-29 3 → 2026-11-27 5（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `05beb527600c` · [字段定义](../../DATASET.md)*
