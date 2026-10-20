# AI Repo Atlas

> 42,853 个 GitHub AI 仓库的中立编目:一仓一张解读卡——机器筛得动、人看得懂、证据可回溯。

![repos](https://img.shields.io/badge/repos-42%2C853-blue) ![cards](https://img.shields.io/badge/deep_cards-668-orange) ![update](https://img.shields.io/badge/update-daily-brightgreen) ![license](https://img.shields.io/badge/data-CC_BY_4.0-lightgrey)

## 这是什么

GitHub 上的开源 AI 项目有几十万个,README 长短不一、真假混杂、中英文都有。本项目把它们变成一张张标准卡片,每张卡片回答选型四问:**它是什么、给谁用、怎么装、有什么限制**——并且每个判断都标注 README 原文行号,可以回链核查。

- **中立编目,不做评价**:README 里的营销语言不会渗透进卡片;只陈述可验证的事实。
- **宁可空,不可猜**:文本里没有的信息是 `null`,不是猜的。
- **元数据反作弊**:许可证以 GitHub 仓库实况为准,不信 README 徽章。

## 数字(2026-10-20)

| 指标 | 数 |
|---|---|
| 覆盖仓库池 | 42,853 |
| 深度解读卡(A 层) | 668(放量至 ~8,000 中) |
| 带维护信号 / 下载信号 | 593 / 278 |
| 带场景标签 | 574([受控词表 47 标签](data/vocab.json)) |
| 商业替代映射 | 1 个产品 |
| 更新频率 | 每日 |

## 三种用法

**人看**——每仓一张 markdown 卡,按首字母浏览 [`data/cards/`](data/cards)。

**程序用**——一行一仓的 JSONL 主表,带 [JSON Schema](data/schema/card.schema.json):
```bash
jq -c 'select(.filters.license_risk=="permissive" and .meta.stars>10000)' data/catalog.jsonl
```

**AI 助手用**——根目录 [`llms.txt`](llms.txt) 是标准发现入口;场景词表在 [`data/vocab.json`](data/vocab.json)。

## 自动生成流水线

本仓卡片由每小时自动流水线生成并发布(断点续传,进度见 [PROGRESS.md](PROGRESS.md)):

1. 检出公开工厂仓(README 43k 份 + 池元数据)——只读输入,零令牌;
2. s8 解读(六道闸 + 行号证据,双跑一致率 98.5%)→ s10 受控词表打标 → s12 每日曲线点;
3. s11 导出(catalog.jsonl + 人读卡 + 曲线)→ 剥离内部字段 → 提交发布。

手动触发一批:[Actions · generate cards](../../actions/workflows/generate.yml)。

## 许可

- 卡片与衍生数据:**CC BY 4.0**。
- 元数据来自 GitHub 公开 API;行号级引文版权归原项目所有,卡片均附原仓库链接。
- 本仓**不收录 README 全文**,只有解读、短引文与回链。

## Roadmap

- [x] A 层卡片 668 张 + 场景词表 v1.0(2026-10-20)
- [ ] A 层放量至 ~8,000
- [ ] B 层迷你卡 34,000
- [ ] 静态站点(搜索/对比/替代页)
- [ ] MCP 服务(AI 助手直接查询本数据)
- [ ] HuggingFace 数据集镜像

## 引用

```bibtex
@dataset{ai_repo_atlas,
  title  = {AI Repo Atlas: a neutral catalog of 42k+ open-source AI repositories},
  author = {AI Repo Atlas},
  year   = {2026},
  url    = {https://github.com/ai-repo-atlas/ai-repo-atlas}
}
```
