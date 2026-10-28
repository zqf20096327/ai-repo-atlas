# tsoj/Chess_diagram_to_FEN

⭐ 35 · Python · MIT · 推送 2026-03-11 · [GitHub](https://github.com/tsoj/Chess_diagram_to_FEN) · 个人维护

**从国际象棋/象棋/将棋棋盘图片中识别并输出 FEN**

基于 PyTorch/torchvision 预训练卷积模型的棋盘图识别工具：多步流程检测图中是否存在棋盘、定位边界框、判断 0/90/180/270 度旋转、逐格预测棋子生成 FEN，并用全连接网络判断视角（黑方/白方）。支持 chess、xiangqi、shogi 三种棋类，其中 shogi 效果较差且不处理持子。提供预训练模型下载脚本，也可自行生成训练数据并训练全部模型。以 Python 库或 CLI 形式使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多步流水线：棋盘检测→边界框→旋转判定→逐格棋子识别→FEN 生成
- 支持 chess、xiangqi、shogi 三种棋类的图片
- 提供预训练模型下载，也支持自行生成数据并训练各阶段模型
- 提供 Python API（get_fen）与演示 CLI

## 适用场景

- 从书籍截图或网页截图中提取棋局 FEN 以便复盘分析
- 批量识别棋类视频/图片中的局面
- 研究棋盘检测与棋子分类的计算机视觉流水线

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Extract the FEN out of images of chess, xiangqi, or shogi diagrams.
> L9: 4. Finally detect the FEN by looking at each square tile and predicting the piece
> L12: All these steps (except the 5th) basically use some common pretrained convolutional models available via torchvisio

## 星数曲线

```mermaid
xychart-beta
    title "tsoj/Chess_diagram_to_FEN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `eae524753434` · [字段定义](../../DATASET.md)*
