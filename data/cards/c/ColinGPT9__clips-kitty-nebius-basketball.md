# ColinGPT9/clips-kitty-nebius-basketball

⭐ 3 · Python · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/ColinGPT9/clips-kitty-nebius-basketball) · 个人维护

**把篮球比赛录像转成竖版集锦片段的开源视频剪辑工具**

本仓库是 Clips Kitty 的 Nebius×NVIDIA 黑客松版本：输入一场篮球比赛（文件或 URL），用 Whisper 转录解说、PANNs 识别观众与哨声、RapidOCR 读取记分牌与比赛时钟、YOLO/OpenCV 分析镜头，Nemotron（经 Nebius Token Factory 的 OpenAI 兼容 API）对片段评分排序并撰写标题，E-BARD 检测球、篮筐与人员实现 9:16 追踪裁切。语言模型通过创作者自己的 Nebius key 直接调用，无中间服务器。仅覆盖黑客松新增内容，其余功能见原仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Nemotron 评分片段并撰写标题，标题经记分牌校验后重写
- E-BARD（YOLOv8n）逐帧检测实现 9:16 追踪裁切
- 冻结证据基准脚本可在同一证据上重放不同模型
- Nemotron 列表下不分发模型权重，仅以托管 API 调用

## 适用场景

- 把整场比赛转成竖版社媒集锦片段
- 在创作者自己的 Nebius key 上以极低成本处理比赛
- 用冻结证据基准对比不同语言模型在相同输入下的表现

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Turn a basketball game into vertical highlight clips. NVIDIA Nemotron on Nebius Token Factory picks the plays and 
> L24: 2. **Asks Nemotron which plays are worth posting.** Nemotron scores the
> L35: The language model is called on the creator's own Nebius key, with no server in

## 星数曲线

```mermaid
xychart-beta
    title "ColinGPT9/clips-kitty-nebius-basketball 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-23 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `1e4d9579a54a` · [字段定义](../../DATASET.md)*
