# vandroogenbroeckmarc/doi2bib

⭐ 43 · TeX · AGPL-3.0 · 推送 2026-06-02 · [GitHub](https://github.com/vandroogenbroeckmarc/doi2bib) · 个人维护

**科研作者用：把 DOI/arXiv 链接转换为规范 BiBTeX 条目**

命令行工具，读取 DOI、完整 URL 或 arXiv 链接，经 CrossRef 与 Unpaywall API 查询并生成 BiBTeX 条目：修正错误字段、按“作者-年份-标题词”重排引用键、用 STRING 宏或 LTWA 标准缩写替换期刊/会议名、将 unicode 转 ASCII、处理标题大写并猜测页码。初始面向电气工程与计算机（含 CV/ML）领域调校，通过环境变量配置缩写库与 API 邮箱；作者自述约九成以上条目正确，仍可能存在错漏。安装方式为 git clone 后 pip 安装依赖，暂未提供 pip 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DOI/arXiv 链接（含非正式 DOI 的 arXiv URL）转 BiBTeX
- 作者-年份-标题词的引用键命名规则
- 期刊/会议名 STRING 宏替换与 LTWA 缩写建议（abbreviation.bib）
- unicode 转 ASCII、标题大写保护与页码自动猜测

## 适用场景

- 写论文时批量把 DOI 转成可用的 BiBTeX 条目
- 统一参考文献中期刊/会议名的长短期缩写格式
- 处理 arXiv 预印本条目的字段规范化

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # doi2bib : yet another tool to generate a BiBTeX entry based on a DOI
> L31: This "doi2bib" version was initially *tuned* for the scientific domains of electrical engineering and computer scie

## 星数曲线

```mermaid
xychart-beta
    title "vandroogenbroeckmarc/doi2bib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `62bc65a4fd7d` · [字段定义](../../DATASET.md)*
