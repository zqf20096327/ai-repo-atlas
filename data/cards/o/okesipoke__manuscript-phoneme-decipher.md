# okesipoke/manuscript-phoneme-decipher

⭐ 118 · HTML · 推送 2026-10-24 · [GitHub](https://github.com/okesipoke/manuscript-phoneme-decipher) · 个人维护

**面向未解读文字的语音转写重建引擎：输出 IPA 假设与置信度**

LinguaCryptum 是一个将未知文字视为语音记录而非字母密码的推理引擎：用户输入手稿图像或字符序列，引擎经字形切分、特征提取、语音候选生成、词库匹配与音系法则校验五个步骤，输出 IPA 音标转写、置信度与可视化映射图。内置源自伏尼契手稿–Elu-Sinhala 项目的 4,591 条语音词形参考词库，提供统计验证套件（响度序列、最小对密度、熵分析）与 HTML5/JS 响应式界面，支持南亚多语言界面切换。README 明确声明输出为计算假设而非已证翻译，仅限学术与文化保护用途，贡献需经两名成员评审。仓库含 Python 与 C 绑定核心引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五步推理流程：字形切分→特征提取→语音候选→词库匹配→音系法则校验
- 4,591 条含声谱指纹的语音参考词库
- 统计验证套件：响度序列原则、最小对密度、熵分析
- HTML5/JS 响应式界面，支持 7 种南亚语言界面切换

## 适用场景

- 处理喜马拉雅或斯里兰卡寺院传统的未出版手稿
- 对磨损刻文做概率性缺字填补
- 为记录濒危语言非标准拼写的语言学田野标注
- 比较宗教灵语文本与自然语音模式

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L44: LinguaCryptum models the act of **speaking a dead language**. You provide a digitized manuscript image or a charact
> L52: The output is a **phonetic transcription in IPA** alongside a **confidence score** and a **visual resonance map** (

## 星数曲线

```mermaid
xychart-beta
    title "okesipoke/manuscript-phoneme-decipher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-24 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `ef0891467653` · [字段定义](../../DATASET.md)*
