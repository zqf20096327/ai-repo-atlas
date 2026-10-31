# kuraneko1/qwen21-fast-comfyui

⭐ 18 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/kuraneko1/qwen21-fast-comfyui) · 个人维护

**在 RTX 4070 12GB 的 ComfyUI 上运行 Qwen-Image-2.1 的设置备忘录与脚本集**

作者在自己 PC（Ubuntu 24.04 + RTX 4070 12GB）上运行 Qwen-Image-2.1 图像生成/编辑模型的手順记录：提供 install.sh 一键脚本下载约17GB量化权重、ComfyUI 自定义节点（Qwen 2.1 Fast Generate）与 3 个工作流，也支持从零安装 ComfyUI 本体；附 CLI 测试脚本与图像编辑示例（炎/水中/雨三场景及提示词）。作者声明这是初学者备忘录、无运行保证，前提为 Linux，Windows/macOS 不能直接运行。实测 1024×1024 约需 10 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- install.sh 支持已有 ComfyUI（A）与新装 ComfyUI（B）两种路径，含 --dry-run
- 附带 1 个自定义节点与 3 个工作流（文生图、随机 seed 编辑、固定 seed 编辑）
- CLI 测试脚本 test_qwen21.py / test_qwen21_edit.py 覆盖生成与编辑
- 记录了 RTX 4070 12GB 的实测生成速度与编辑提示词技巧

## 适用场景

- 在 12GB 显存 GPU 上用 ComfyUI 跑 Qwen-Image-2.1 的文生图与图像编辑
- 通过固定 seed 工作流复现示例图片
- 参照提示词写法做保持角色一致性的场景编辑

## 场景标签

`图像生成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L3: # 12GBのGPUで Qwen-Image-2.1 を ComfyUI で動かす（初心者の備忘録）
> L13: > **初心者の備忘録です。** 自分のPCで動いた手順を残しています。
> L17: ComfyUIをすでに使っている人も、これから入れる人も、**ノードを1個**追加して画像生成と編集を試せます。

## 星数曲线

```mermaid
xychart-beta
    title "kuraneko1/qwen21-fast-comfyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6b05f763bf8b` · [字段定义](../../DATASET.md)*
