# debs-obrien/grading-buddy-lfm3-demo

⭐ 3 · TypeScript · MIT · 推送 2026-11-11 · [GitHub](https://github.com/debs-obrien/grading-buddy-lfm3-demo) · [官网](https://grading-buddy-lfm3-demo.pages.dev) · 个人维护

**离线浏览器端小模型问答工具：帮孩子备考 ITF 跆拳道白黄带考核**

一个在桌面浏览器本地运行 LFM3-1.7B（Transformers.js + WebGPU）的问答应用，模型下载约 1.1 GB 后可完全离线使用，无服务器与 API key。应用仅依据作者核对过的考核笔记回答：先做主题匹配，命中才调用模型并要求其从笔记事实生成一两句回答，随后通过术语/数字等 grounding 检查，失败则回退显示笔记卡片，范围外问题直接拒绝。考核测验与判分由纯代码实现；提供 Node CPU 环境的 frozen 评测脚本。仅支持具备 WebGPU 的桌面浏览器，iPhone 加载失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LFM3-1.7B 通过 Transformers.js 在浏览器 WebGPU 上离线推理
- 主题匹配 + grounding/必需事实检查，未通过则回退到笔记卡片
- 范围外问题在调用模型前拒绝；测验判分为纯代码
- 提供 Node CPU 冻结问题集评测（npm run eval）

## 适用场景

- 孩子课后离线练习跆拳道白黄带的韩语术语、 tenets 与套路
- 仅依据可信笔记回答、拒答范围外问题的本地问答场景
- 参考 examples/minimal 单页加载并试用 LFM3 模型

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: Can a small Liquid model do a real job with no signal? I built a study buddy for my kids' first Taekwon-Do gradings 
> L40: - LFM3-1.7B (q4f16) runs in a Web Worker on WebGPU with Transformers.js.
> L44: - The model is asked to answer in a sentence or two from those facts. A grounding check (Korean terms, numbers, typ

## 星数曲线

```mermaid
xychart-beta
    title "debs-obrien/grading-buddy-lfm3-demo 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `1494ef3c1f5d` · [字段定义](../../DATASET.md)*
