# ryan-he-47/Vibe-OOP-Flowchart-to-Code

⭐ 14 · Python · MIT · 推送 2026-04-16 · [GitHub](https://github.com/ryan-he-47/Vibe-OOP-Flowchart-to-Code) · 个人维护 · 中文 README

**用 Mermaid 流程图作结构化提示词生成代码的 PoC 编辑器**

概念验证原型：以模板化 Mermaid 流程框图描述程序结构，提供 program/module/class/function 等语义模板，支持图形化编辑节点、显式定义输入/输出与成员变量、通过端口连线表达数据流，并导入/导出 .mmd 文件。导出的流程图作为 vibe coding 的结构化提示词喂给大模型，可一键导出无元数据的纯净 .mmd 以降低 token 开销。面向采用大模型辅助编程的开发者与希望降低提示词撰写门槛的非专业人士。仓库自述代码几乎全部由 GitHub Copilot 生成且未经系统性人工审查，界面与交互较为朴素，不适合当作生产级编辑器。

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

- program/module/class/function 等模板化节点表示语义角色
- 显式编辑输入、输出、成员变量并用端口连线表达约束关系
- 导入/导出 Mermaid .mmd 文件并在文本中嵌入元数据保留布局
- 一键导出无 VC_METADATA 的纯净 .mmd，降低喂给大模型的 token 开销

## 适用场景

- 把复杂程序结构画成流程图，作为大模型生成代码的结构化提示词
- 多人协作迭代提示词时以分块、分层的框图替代松散文本
- 非专业人士用图形方式快速描述程序流程再交给 AI 实现

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L7: 我的核心想法很简单：**在 vibe coding 这种大模型参与度很高的开发方式里，纯文本提示词常常太松散、太难维护**。而流程框图天然更结构化，尤其是 Mermaid 这种轻量、可读、可编辑的图形语言，大语言模型对它的理解通常也
> L112: 5. 导出 `.mmd` 文件，作为后续 vibe coding 的结构化提示词。
> L113: 6. 随便找个能读.mmd的agent喂给它

## 星数曲线

```mermaid
xychart-beta
    title "ryan-he-47/Vibe-OOP-Flowchart-to-Code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `9dead68ca779` · [字段定义](../../DATASET.md)*
