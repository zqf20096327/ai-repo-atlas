# juanmanueldaza/linkedin2md

⭐ 47 · Python · GPL-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/juanmanueldaza/linkedin2md) · [官网](https://linkedin2md.daza.ar) · 个人维护

**把 LinkedIn 数据导出转为 Markdown 与 PDF 简历的零依赖 Python CLI**

面向求职者与职场用户的命令行工具：读取 LinkedIn 官方数据导出 ZIP，解析为 40+ 个按类别组织的 Markdown 文件（经历、技能、推荐信、求职申请、隐私数据等），可选生成 A4 PDF 简历（需额外安装 weasyprint 与 markdown）。输出格式便于导入 NotebookLM、Claude Projects、Ollama 等 LLM 工具做职业分析。零依赖核心，通过 pipx/pip 安装，支持英文与西班牙文输出及 JSON 诊断报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LinkedIn 导出 ZIP 解析为 40+ 分类 Markdown 文件
- 可选生成 A4 PDF 简历（依赖 weasyprint/markdown，未安装则跳过）
- 支持 en/es 输出语言与 JSON 转换诊断报告
- pipx/pip 安装，核心零依赖

## 适用场景

- 把 LinkedIn 档案转成 Markdown 供 LLM 分析职业经历
- 生成 PDF 简历用于求职
- 查看并归档 LinkedIn 掌握的个人全部数据

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L12: Convert LinkedIn data exports to clean Markdown files - the ideal format for LLM analysis.
> L16: Markdown is the lingua franca of AI tools. Once your LinkedIn data is in `.md` format, you can:
> L18: - **Upload to NotebookLM** and have conversations about your career history

## 星数曲线

```mermaid
xychart-beta
    title "juanmanueldaza/linkedin2md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-25 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c7d166fa58a9` · [字段定义](../../DATASET.md)*
