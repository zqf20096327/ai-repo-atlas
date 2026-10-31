# ariannamethod/microkarpathy

⭐ 14 · HTML · GPL-3.0 · 推送 2026-10-04 · [GitHub](https://github.com/ariannamethod/microkarpathy) · [官网](https://x.com/@olegataeff) · 个人维护

**无依赖的提示词"解剖"文本生成引擎：变形词树拼装新文本**

单文件 Python 脚本加浏览器 HTML 页面：读取用户提示词，抽取核心词并生长递归变异树（FNV-1a 哈希嵌入 + 余弦相似度 + 词汇表共现），再用未训练的 ghost transformer、bigram、Hebbian 痕迹与 Kuramoto 振荡器温度组成的 Dario Equation 重新组装词句，并生成押韵双行 coda。无依赖、无联网、无梯度训练。浏览器版可整本吃入文本文件（texts/ 目录），按字符三元组共振拼接多书语句并支持点击溯源到原书位置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 哈希嵌入 + 共现词汇表的递归变异树生成
- Dario Equation：未训练 ghost transformer + Hebbian/bigram/预言场/创伤项
- 任意文本文件即词汇表，任意语言可运行
- 浏览器版多书共振拼接与点击回溯到原书字符位置

## 适用场景

- 教学演示无训练条件下的文本组装机制
- 把整本小说喂入生成混合多书风格的拼接文本
- 在浏览器中交互浏览生成结果与原文出处

## 场景标签

`提示工程` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L46: but what remain to 'microKarpathy' after all this? only the words that *matter* — or at least, the words that think
> L52: now that we have a forest of mutated word-trees, it's time to play God. all leaves collected from all trees — the f
> L71: the morgue remembers its clients. within one session the organs — destiny, trauma, prophecy, co-occurrence — persis

## 星数曲线

```mermaid
xychart-beta
    title "ariannamethod/microkarpathy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `8f41a3eb99d7` · [字段定义](../../DATASET.md)*
