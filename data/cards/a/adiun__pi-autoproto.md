# adiun/pi-autoproto

⭐ 14 · Python · MIT · 推送 2026-06-28 · [GitHub](https://github.com/adiun/pi-autoproto) · 个人维护

**给 pi agent 的原型构建-评测循环：合成人格真实试用并迭代**

pi-autoproto 是 pi 编码 agent 的扩展与技能包，面向产品早期探索：定义目标人格与应用假设后，由独立进程中的合成人格在真实浏览器中点击、填写表单试用原型，产出任务评分与逐字反馈；编码 agent 据此修改代码，按 keep/discard 分数棘轮迭代。支持 agent-browser（视觉）与 playwright-cli（文本）两种浏览器后端，含优先级加权评分、人格行为变体、探索性任务与比较报告机制。README 声明项目处于早期粗糙阶段，合成人格不能替代真实用户研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 合成人格在真实浏览器中黑盒试用原型并输出逐字反馈
- keep/discard 分数棘轮驱动的自主构建-评测循环
- 优先级加权评分（P0×0.60+P1×0.25+P2×0.15），P0 失败封顶 40 分
- 自动生成四个人格行为变体独立评测，附谄媚偏差检测

## 适用场景

- 产品早期让合成用户试用原型、暴露交互摩擦点
- 对比多种 UX 方向的原型并生成结构化比较报告
- 为真实用户研究生成可验证的假设

## 场景标签

`浏览器自动化` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L3: Persona-driven UX evaluation for pi, inspired by ideas from autoresearch.
> L136: The package has two parts: an **extension** (tools, state, UI) and a **skill** (workflow knowledge). Prototype app

## 星数曲线

```mermaid
xychart-beta
    title "adiun/pi-autoproto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `355badac647f` · [字段定义](../../DATASET.md)*
